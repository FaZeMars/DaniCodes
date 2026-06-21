def main():
    camel_case = input("camelCase: ")
    for letra in camel_case:
        if letra.isupper():
                print("_", letra.lowercase(), end="")

main()
