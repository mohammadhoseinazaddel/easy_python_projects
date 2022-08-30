import string
from random import choices

def create_password(length=5, upper=False, lower=False, digit=False, pun=False):
    pool=''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == '':
        pool = string.ascii_letters

    return ''.join(choices(pool, k=length))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(create_password())
    print(create_password(upper=True))
    print(create_password(10,upper=True))
    print(create_password(upper=True ,lower=True))
    print(create_password(10, upper=True ,lower=True))
    print(create_password(upper=True ,lower=True, digit=True))
    print(create_password(10,upper=True ,lower=True, digit=True))
    print(create_password(upper=True ,lower=True, digit=True, pun=True))
    print(create_password(20, upper=True ,lower=True, digit=True, pun=True))
