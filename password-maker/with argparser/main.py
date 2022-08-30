import string
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-u', '--upper',  help="use upper case", action='store_true') #-u is optional but u is required(positional)
    parser.add_argument('-l', '--lower',  help="use lower case", action='store_true') #action=store_true does it need number 1 0 after it or it is look like -f
    parser.add_argument('-d', '--digit',  help="use digits case", action='store_true')
    parser.add_argument('-p', '--pun',  help="use punctuation case", action='store_true')


    args = parser.parse_args()
    print(args)

    print(create_password(
        args.length, args.upper, args.lower, args.digit, args.pun
    ))




