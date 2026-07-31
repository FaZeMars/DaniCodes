import re
import inflect
import sys
from datetime import date

p = inflect.engine()
class Birth:

    def __init__(self, birthdate):
        self.birthdate = birthdate




    @classmethod
    def get(cls):
        birthdate = input("Date of Birth: ")
        return cls(birthdate)

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        birthdate = birthdate.strip()
        matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birthdate)
        if matches:
            yyyy, mm, dd = int(matches.group(1)), int(matches.group(2)), int(matches.group(3))

            try:
                self._birthdate = date(yyyy, mm, dd)
            except (ValueError, TypeError):
                sys.exit("Invalid Date")
        else:
            sys.exit("Invalid Date")

    def convert(self):
        today = date.today()
        difference = (today - self._birthdate).days
        minutes = difference * 24 * 60
        words = p.number_to_words(minutes, andword="")
        return f"{words.capitalize()} minutes"

def main():
    birth = Birth.get()
    print(birth)


if __name__ == "__main__":
    main()
