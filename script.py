import re

SKYPES = re.compile(r'\bskype:[a-zA-Z0-9]+')
EMAILS = re.compile(
    r'\b[a-zA-Z0-9][a-zA-Z0-9.+\-_]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.+\-_]+\.[a-zA-Z0-9.+\-_]+[a-zA-Z0-9]\b')
PHONES = re.compile(r'\+\d{1,3}\s\d{3}\s\d{3}\s\d{3}\b')


def validate_character(character):
    if not len(character) == 1:
        raise ValueError('Character must be only 1 symbol')
    return True


def skype_user_anomin(line, character):
    if validate_character(character):
        res = SKYPES.sub(f'skype:{character}', line)
        return res


def additional_verif_email(line):
    inc = 0
    for i in line:
        if i == '+' or i == '.' or i == '-':
            inc += 1
        else:
            inc = 0
        if inc == 2:
            return True
    return False


def email_anonim(line, character):
    emails = EMAILS.findall(line)
    new_emails = dict()

    for i, email in enumerate(emails):
        if not additional_verif_email(email):
            username = email[:email.index('@')]
            domain = email[email.index('@'):]
            if len(username) == 2:
                new_emails[email] = username[0] + character + domain  # если у нас емейл ss@gmail.com - > s#gmail.com
            else:
                new_emails[email] = username[0] + character * (len(username) - 2) + username[-1] + domain
    res = line

    for key, val in new_emails.items():
        res = res.replace(key, val)

    return res


def phone_anonim(line, character, num):
    phones = PHONES.findall(line)
    inc = 0
    new_phones = dict()

    if 0 <= num <= 9:  # max number of hidden digits.
        for phone in phones:
            new_phone = list(phone)

            for i, _ in enumerate(new_phone):

                if num == inc:
                    break

                if new_phone[len(new_phone) - 1 - i] != ' ':
                    new_phone[len(new_phone) - 1 - i] = character
                    inc += 1

            inc = 0
            new_phones[phone] = ''.join(new_phone)
    else:
        raise ValueError("Incorrect number of digits")

    res = line
    for key, val in new_phones.items():
        res = res.replace(key, val)

    return res

