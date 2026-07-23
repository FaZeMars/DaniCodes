import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    #                             1               2          3                4         5            6
    matches = re.search(r"^([0-1]?[0-9]+):([0-5]?[0-9]?) (AM|PM) to ([0-1]?[0-9]?):([0-5]?[0-9]?) (AM|PM)", s)
    if matches:
        s1, s2, s3 = matches.group(1), matches.group(2), matches.group(3)
        s4, s5, s6 = matches.group(4), matches.group(5), matches.group(6)
        try:



            if int(s1) > 12 or int(s4) > 12:
                raise ValueError

            if not (s3 == "AM" or s3 == "PM") or not (s6 == "AM" or s6 == "PM")
                raise ValueError


            








        except ValueError:
            sys.exit("Enter a valid time")





if __name__ == "__main__":
    main()




#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM
