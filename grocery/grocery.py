def main():

    list = get_list("")
    print(list)

def get_list(s):
    empty = {}
    while True:

        try:
            groc = input("").upper()
            empty[groc] = groc
            comp = count(empty[groc])


        except EOFError:
            print("")
            return comp




main()

