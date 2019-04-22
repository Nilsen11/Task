import re

SKYPES = re.compile(r'\bskype:[a-zA-Z0-9]+')
EMAILS = re.compile(
    r'[a-zA-Z0-9][a-zA-Z0-9.+\-_]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.+\-_]+\.[a-zA-Z0-9.+\-_]+[a-zA-Z0-9]\b')
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
        if i == '+' or i == '.' or i == '-':  # если у нас емейл sss..as@gmail.com или sss.s@gmails..com - > Ошибка
            inc += 1
        else:
            inc = 0
        if inc == 2:
            return True
    return False


def email_anonim(line, character):
    if validate_character(character):
        emails = EMAILS.findall(line)
        new_emails = dict()

        for i, email in enumerate(emails):
            if not additional_verif_email(email):
                username = email[:email.index('@')]
                domain = email[email.index('@'):]
                if len(username) == 2:  # если у нас емейл: ss@gmail.com - > s#gmail.com
                    new_emails[email] = username[0] + character + domain
                else:
                    new_emails[email] = username[0] + character * (len(username) - 2) + username[-1] + domain
        res = line

        for key, val in new_emails.items():
            res = res.replace(key, val)

        return res


def phone_anonim(line, character, num):
    if validate_character(character):
        phones = PHONES.findall(line)
        inc = 0
        new_phones = dict()

        if 0 <= num <= 9:  # code is always available. - > +7 ### ### ### or +38 ### ### ###
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
