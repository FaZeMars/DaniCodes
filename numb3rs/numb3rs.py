import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if match:
        first = int(match.group(1))
        second = int(match.group(2))
        third = int(match.group(3))
        fourth = int(match.group(4))

        if  0 <= first <= 255 and 0 <= second <= 255 and 0 <= third <= 255 and 0 <= fourth <= 255:
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    main()
