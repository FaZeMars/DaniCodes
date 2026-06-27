def main():

    list = get_list("")
    print(list)

def get_list(s):
    while True:
        empty = {}
        try:
            groc = input("").upper()
            empty[groc] = groc


        except EOFError:
            print("")
            return empty[groc]




main()

