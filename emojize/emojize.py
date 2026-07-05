import emoji # type: ignore
import sys

def main():
    string = input("Input: ")
    for alia in "alias":
        if alia in string:
            s = emoji.emojize(string(alia), language='alias')
            print(s)



main()
