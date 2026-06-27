def main():

    list = get_list("")
    print(list)

def get_list(s):
    empty = {}
    while True:

        try:
            groc = input("").upper()
            if groc in empty:
                empty[groc] += 1
            else :
                empty[groc] = 1


        except EOFError:
            print("")
            return empty




main()

