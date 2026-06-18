def main():
    expression = input("Expression: ")
    parts = expression.split(" ")

    x = int(parts[0])
    y = parts[1]
    z = int(parts[2])

    if y == "+":
        result = float(x + z)
    elif y == "-":
        result = float(x - z)
    elif y == "*":
        result = float(x * z)
    elif y == "/":
        result = float(x / z)

    print(result)


main()










