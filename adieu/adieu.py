import inflect
p = inflect.engine()

def main():


    x = []
    while True:
        try:
            user_input = input("Name: ")
            x.append(user_input)
        except EOFError:
            break
    print()

    final = p.join(x)
    print(f"Adieu, adieu, to {final}")

main()
