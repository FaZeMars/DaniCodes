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

            elif month.isdigit() and 0 < int(month) <= 12 and 0 < int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

        except (ValueError, IndexError, AttributeError):
            pass
        except EOFError:
            print("")
            break


def get_int(s):
    inp = input(s).strip()
    if "/" in inp:
        x = inp.split("/")
        if len(x) == 3 and x[0].isdigit():
            return x[0], x[1], x[2]
        raise ValueError

    elif "," in inp:
        z = inp.replace(",", "").title()
        x = z.split()
        if len(x) == 3 and x[0] in [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]:
            return x[0], x[1], x[2]
        raise ValueError

    else:
        raise ValueError


main()
