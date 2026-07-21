import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'^<iframe .*?src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)".*?></iframe>$', s)
    if matches:
        id = matches.group(1)
        realid = f"https://youtu.be/{id}"
        return realid
    else:
       return None



if __name__ == "__main__":
    main()



