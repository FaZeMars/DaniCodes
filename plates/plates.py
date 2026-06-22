def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


valid = []

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for pla in plate:
        





main()
