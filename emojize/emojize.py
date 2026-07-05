import emoji # type: ignore
import sys

def main():
    string = input("Input: ")
    emoj = emoji.emojize(string, language='alias')
    print(emoj)


main()
