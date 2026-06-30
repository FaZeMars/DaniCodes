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



    month, day, year = get_int("Date: ")




    if month in valid:
        print(f"{year}-{valid[month]}-{int(day):02}")

    elif not month in valid:
        print(f"{year}-{int(month):02}-{int(day):02}", end= "")

    else:
        return



def get_int(s):
    while True:
        try:

            inp = input(s)
            if "/" in inp:
                x = inp.split("/")
                if 0 < int(x[1]) <= 31:
                    return x[0], x[1], x[2]
                else:
                    pass

            elif "," in inp:
                z = inp.replace(",", "").title()
                x = z.split()
                if 0 < int(x[1]) <= 31:
                    return x[0], x[1], x[2]
                else:
                    pass

            else:
                print("")
                pass

        except ValueError:
            print("")
            break

        except EOFError:
            print("")
            break


main()



