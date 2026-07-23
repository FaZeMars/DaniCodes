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



            if int(s1) > 12 or int(s2) > 59 or int(s4) > 12 or int(s5) > 59:
                raise ValueError

            elif int(s1) < 0 or int(s2) < 0 or int(s4) < 0 or int(s5) < 0:
                raise ValueError

            elif not (s3 == "AM" or s3 == "PM") or (s6 == "AM" or s6 == "PM"):
                raise ValueError

            elif s2 == None:
                s2 = "00"

            elif s5 == None:
                s5 = "00"

            elif s3 == "AM":
                if s1 == "12":
                    s1 == "0"

            elif s6 == "AM":
                if s4 == "12":
                    s4 == "0"

            elif s3 == "PM":
                if 0 < int(s1) < 12:
                    int(s1) + 12

            elif s6 == "PM":
                if 0 < int(s3) < 12:
                    int(s3) + 12

            else:
                print(")









        except ValueError:
            sys.exit("Enter a valid time")





if __name__ == "__main__":
    main()




#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM
