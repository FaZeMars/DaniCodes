import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    match = re.search(r"^(d+)\.(d+)\.(d+)\.(d+)", ip)
    if match:
        first = int(match.group(1))
        second = int(match.group(2))
        third = int(match.group(3))
        fourth = int(match.group(4))

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
