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
        try:
            counter = 0
            if 0 < first <= 255:
                counter += 1
            if 0 < second <= 255:
                counter += 1
            if 0 < third <= 255:
                counter += 1
            if 0 < fourth <= 255:
                counter += 1
            else:
                counter = 0
        except ValueError:








if __name__ == "__main__":
    main()
