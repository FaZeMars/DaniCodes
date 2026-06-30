def main():
    valid = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    inputt = get_int("Date: ")
    print(inputt)



def get_int(s):
    while True:
        try:
            inp = input(s)
            if "/" in inp:
                inp.split("/","")
                return inp[0], inp[1], inp[2]

            elif "," in inp:
                inp.replace(",", " ").split(" ")
                return inp[0], inp[1], inp[2]
            else:
                pass

        except ValueError:
            pass

        except EOFError:
            print("")
            break


main()



