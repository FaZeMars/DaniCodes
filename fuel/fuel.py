def main():

    inp = input("Fraction: ")
    part1, part2 = inp.split("/")
    num1 = int(part1)
    num2 = int(part2)

    if w == 0:
        print("E")



    while 0 <= num1 <= num2:
        if  0 < num1 < num2:
            try:
                z = num1 / num2
                q = z * 100
                w = q.round()
                return w

            except (ValueError):
                pass
            except (ZeroDivisionError):
                return w == 0





main()













main()































