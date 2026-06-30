def main():
    valid = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }


    while True:
        try:
            year, month, day = get_int()
            if month in valid:
                print(f"{year}-{valid[month]}-{int(day):02}")

            elif not month in valid:
                print(f"{year}-{int(month):02}-{int(day):02}", end= "")

            else:
                return

        except ValueError:
            pass

        except EOFError:
            print("")
            break




def get_int(s):
            inp = input("Date: ")
            if "/" in inp:
                x = inp.split("/")
                if 0 < int(x[1]) <= 31:
                    return x[0], x[1], x[2]
                else:
                    raise ValueError

            elif "," in inp:
                z = inp.replace(",", "").title()
                x = z.split()
                if 0 < int(x[1]) <= 31:
                    return x[0], x[1], x[2]
                else:
                    raise ValueError
            else:
                raise ValueError







main()



