import re
from pprint import pprint


def skype_user_anomin(line, character):
    # return re.findall(r'\bskype:[a-zA-Z0-9]+', str)
    res = re.sub(r'\bskype:[a-zA-Z0-9]+', f'skype:{character}', line)
    return res


str1 = "skype:hfgh?;skype:nilsen-ss!"

str2 = "Lorem ipsum <a href=”skype:loremipsum?call”>call</a>,dolor sit"

str3 = ";skype:hfg-h "

str4 = "sit <a href=”skype:IPSUMLOREM?chat”>chat</a> amet. Lorem skype:ipsum sit SKYPE:"


print('*'*100)
print(skype_user_anomin(str1, "#"))
print(skype_user_anomin(str2, "X"))
print(skype_user_anomin(str3, "#"))
print(skype_user_anomin(str4, "*"))
print('*' * 100)


em1 = "jass@gmail.....com abc-abc@abc.edu.co.uk"
em2 = " Lorem abc-abc@abc.edu.co.uk am"
em3 = "Lorem ipsum"
em4 = "Lorem ipsum --@--.--"
em5 = " Lorem ses@data.ua ipsum"


def email_anonim(line, character):
    # return re.findall(r'@\w+\.\w+', str)
    emails = re.findall(
        r'\b[a-zA-Z0-9][a-zA-Z0-9.+\-_]+[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.+\-_]+\.[a-zA-Z0-9.+\-_]+[a-zA-Z0-9]\b',
        line)

    new_emails = dict()

    for i, email in enumerate(emails):
        username = email[:email.index('@')]
        domain = email[email.index('@'):]
        character = character * (len(username) - 2)

        new_emails[email] = username[0] + character + username[-1] + domain

    res = line

    for key, val in new_emails.items():
        res = res.replace(key, val)
        # res = re.sub(key, val, res)

    return res


print(email_anonim(em1, "#"))
print(email_anonim(em2, "#"))
print(email_anonim(em3, "#"))
print(email_anonim(em4, "#"))
print(email_anonim(em5, "#"))
print('*' * 100)


num1 = "+48 845 546 546"
num2 = "Lorem +48 845 546 546 ipsum"
num3 = "Lorem ipsum"
num4 = "Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet"


def phone_anonim(line, character, num):
    phones = re.findall(r'\+\d{1,3}\s\d{3}\s\d{3}\s\d{3}\b', line)
    inc = 0
    new_phones = dict()

    if 0 <= num <= 10:  # max number of hidden digits. +# ### ### ### +38# ### ### ### +3 ## ### ### ###
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
        return "Incorrect number of digits"

    res = line
    for key, val in new_phones.items():
        res = res.replace(key, val)

    return res


print(phone_anonim(num1, "#", 3))
print(phone_anonim(num2, "#", 7))
print(phone_anonim(num3, "#", 9))
print(phone_anonim(num4, "#", 10))
print('*'*100)


# if __name__ == '__main__':
#     try:
#         string = input("Enter input data: \n")
#         symbol = input("Enter mask char: \n")
#
#         print(type(string))
#     except Exception as e:
#         print(type(e), e)
