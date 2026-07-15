import sys
import csv

def main():
    old_file, new_file = validate()
    clean_list = organize(old_file)
    organized_list = newcsv(new_file, clean_list)


def validate():
    command = sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if command[1].endswith(".csv") and command[2].endswith(".csv"):
            return command[1], command[2]

        else:
            sys.exit("Not a CSV file")

def organize(x):
    students = []
    with open(x) as file:
        reader = csv.DictReader(file)
        for row in reader:
            fullname = row["name"]
            house = row["house"]
            last, first = fullname.split(", ")
            students.append({"first": first, "last": last, "house": house})
    return students


def newcsv(x, y):
    columns = ["first", "last", "house"]
    with open(x, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for student in y:
            writer.writerow(student)


if __name__ == "__main__":
    main()
