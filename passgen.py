import random
import string
import sys
import getopt

# Types of password
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIALS = string.punctuation

# Command line options and parameter list
short_options = "luds"
long_options = ["lowercase", "uppercase", "digits", "specials"]
all_arguments = sys.argv
argument_list = all_arguments[1:]


def show_menu():
    print("Usage: python passgen.py -[options] -[length] \n")
    print("Options:\n")
    print("-l --lowercase       Put lowercase characters in your password")
    print("-u --uppercase       Put uppercase characters in your password")
    print("-d --digits          Put digits in your password")
    print("-s --specials        Put special characters in your password")


def generate_password(argv):
    opts, value = getopt.getopt(argument_list, short_options, long_options)
    password_len = int(value[0])
    output_password = ''
    for i, v in opts:
        if i in ("-l", "--lowercase"):
            output_password += LOWERCASE
        if i in ("-u", "--uppercase"):
            output_password += UPPERCASE
        if i in ("-s", "--specials"):
            output_password += SPECIALS
        if i in ("-d", "--digits"):
            output_password += DIGITS

    password_list = list(output_password)
    random.shuffle(password_list)
    output_password = ''.join(random.choices(password_list, k=password_len))
    return output_password


if __name__ == '__main__':
    show_menu()
    print(f"\nPassword generated: {generate_password(sys.argv)}")
