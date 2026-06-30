def main():
    valid = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    }



    year, month, day = get_int("Date: ")



    

    if month in valid:
        print(f"{year}/{month}/{day})
    else:
        return



def get_int(s):
    while True:
        try:
            inp = input(s)
            if "/" in inp:
                x = inp.split("/")
                return x  # 7/7/2011

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



