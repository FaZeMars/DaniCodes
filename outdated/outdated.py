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



    while True:
        for moth in valid:
            if month == moth:
                print(f"{valid[moth]}/{day}/{year}")
                break
            else:
                return



def get_int(s):
    while True:
        try:
            inp = input(s)
            if "/" in inp:
                x = inp.split("/")
                return x[0], x[1], x[2]

            elif "," in inp:

                return inp
            else:
                pass

        except ValueError:
            pass

        except EOFError:
            print("")
            break


main()



