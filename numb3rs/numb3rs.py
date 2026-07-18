import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(d+)\.(d+)\.(d+)\.(d+)", ip)
    if match:
        first = match.group(1)
        second
        third
        fourth






if __name__ == "__main__":
    main()
