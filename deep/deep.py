def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?" )
    answer(x)


def answer(x):
    if x == "42" or x == "forty-two" or x == "forty two":
        print("Yes")
    else:
        print("No")

main()
