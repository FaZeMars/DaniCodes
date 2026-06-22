def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number = False
    for pla in s:
        if pla.isdigit():
            if number == False and pla == "0":
                return False
            number = True

        if pla.isalpha():
            if number == True:
                return False

        if not pla.isalnum():
            return False
    return True



main()
