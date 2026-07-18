import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    first, second, third, fourth = ip.split(".").strip
    if re.search(r"^[0-9])




if __name__ == "__main__":
    main()
