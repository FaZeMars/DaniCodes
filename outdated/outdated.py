def main():
    valid = [
    "January": 1
    "February": 2
    "March": 3
    "April": 4
    "May": 5
    "June": 6
    "July": 7
    "August": 8
    "September": 9
    "October": 10
    "November": 11
    "December": 12
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
                
                return inp
            else:
                pass

        except ValueError:
            pass

        except EOFError:
            print("")
            break


main()



