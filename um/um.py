import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    count = 0
    if matches:
        count += 1
    return count






if __name__ == "__main__":
    main()
