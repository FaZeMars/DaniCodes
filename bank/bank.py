def main():
    greet = input("Greeting: ").lower().strip()
    value(greet)



def value(greet):
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")










main()
