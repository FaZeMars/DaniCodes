import emoji # type: ignore

def main():
    string = input("Input: ")
    emoj = emoji.emojize(string, language='alias')
    print(emoj)


main()
