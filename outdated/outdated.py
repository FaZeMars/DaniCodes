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
            month, day, year = get_int("Date: ")

            if month in valid and 0 < int(day) <= 31:
                print(f"{year}-{valid[month]}-{int(day):02}")
                break

            elif not month in valid and 0 < int(day) <= 31 and 0 < int(month) <= 12:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

            else:
                pass

        except ValueError:
            pass
        except EOFError:
            print("")
            break


def get_int(s):
    inp = input(s).strip()
    if "/" in inp:
        x = inp.split("/")
        return x[0], x[1], x[2]

    elif "," in inp:
        z = inp.replace(",", "").title()
        x = z.split()
        return x[0], x[1], x[2]

    else:
        raise ValueError


main()
