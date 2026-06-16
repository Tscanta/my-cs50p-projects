#VANITY PLATES CHECK!

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #minimum two letters and a maximum of six
    if len(s) < 2 or len(s) > 6:
        return False

    #checking if the first two are alphabets or not
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    #only letters and numbers allowed
    for c in s:
        if not c.isalnum():
            return False

    for pos, c in enumerate(s):
        if c.isdigit():

            #first number cannot be zero
            if c == '0':
                return False

            #everything after first digit must be digits
            for x in s[pos:]:
                if not x.isdigit():
                    return False
            break
    return True

main()
