import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if match:
        first = match.group(1)
        second = match.group(2)
        third = match.group(3)
        fourth = match.group(4)

        if (len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0") or (len(third) > 1 and third[0] == "0") or (len(fourth) > 1 and fourth[0] == "0"):
            return False

        elif  0 <= first <= 255 and 0 <= second <= 255 and 0 <= third <= 255 and 0 <= fourth <= 255:
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    main()
