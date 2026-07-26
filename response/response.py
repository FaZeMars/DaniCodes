from validator_collection import checkers

def main():
    print(emailchecker(input("What's your email adress? ")))




def emailchecker(s):
    mail = checkers.is_email(s)
    try:
        if mail == True:
            return "Valid"

        else:
            return "Invalid"
    except ValueError:
        return "Invalid"





if __name__ == "__main__":
    main()
