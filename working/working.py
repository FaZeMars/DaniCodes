import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    #                             1               2          3                4         5            6
    matches = re.search(r"^([0-1]?[0-9]+):([0-5]?[0-9]?) (AM|PM) to ([0-1]?[0-9]]?):([0-5]?[0-9]?) (AM|PM)", s)
    if matches:
        s1, s2, s3 = int(matches.group(1)), int(matches.group(2)), matches.group(3)
        s4, s5, s6 = int(matches.group(4)), int(matches.group(5)), matches.group(6)
        try:



            if int s1 > 12 or s2 > 59 or s4 > 12 or s5 > 59:
                raise ValueError
            elif s1 < 0 or s2 < 0 or s4 < 0 or s5 < 0:
                raise ValueError

            else:
                if not (s3 == "AM" or s3 == "PM") or (s6 == "AM" or s6 == "PM"):
                    raise ValueError

                elif s3 == "AM":






        except ValueError:
            sys.exit("Enter a valid time")





if __name__ == "__main__":
    main()




#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM
