import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    #                         1          2         6          4         5          6
    matches = re.search(r"^([1]?[0-9]?):([])", s)
    if matches:



if __name__ == "__main__":
    main()




#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM
