import sys
import csv
import tabulate

command = sys.argv


if len(command) == 1:
    sys.exit("Too few command-line arguments")
elif len(command) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        if command[1].endswith(".csv"):
            prices = []
            with open(command[1]) as file:
                reader = csv.DictReader
                for row in reader:
                    prices.append(row)
            print(tabulate)




                    #students.append({"name": row["name"], "home": row["home"]})




        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File not found")







