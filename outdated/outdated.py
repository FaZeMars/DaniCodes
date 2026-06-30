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
        month, day, year = get_int("Date: ")
         try:

            if month in valid and 0 < int(day) <= 31:
                print(f"{year}-{valid[month]}-{int(day): 02}")

            elif not month in valid and 0 < int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}", end= "")

            else:
                raise ValueError

         except ValueError:
            pass
         except EOFError:
             break







def get_int(s):
            inp = input(s)
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



