import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(d+)\.(d+)\.(d+)\.(d+)", ip)
    if match:
        first = match.group(1)
        second = match.group(2)
        third = match.group(3)
        fourth = match.group(4)

        if not 0 < first <= 255:
            return False
        if not 0 < second <= 255:
            return False
        if not 0 < third <= 255:
            return False
        if not 0 < fourth <= 255:
            return False
        else:
            return True
    elif True:
        sys.exit("True")
    else:
        sys.exit("False")

if __name__ == "__main__":
    main()
