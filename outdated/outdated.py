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
    if inputt in valid:



def get_int(s):
    while True:
        try:
            inp = input(s)
            if "/" in inp:
                inp.split("/","")
                return inp[0], inp[1], inp[2]

            elif "," in inp:
                inp.split(" ")



        except ValueError:
            pass

        except EOFError:
            print("")
            break






