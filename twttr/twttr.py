def main():
    text = input("Input: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for vowel in vowels:
        text = text.replace(vowel, "")

    print("Output:", text)

main()











