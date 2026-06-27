def main():

    list = get_list("")

def get_list(s):
    while True:
        empty = {}
        try:
            groc = input("").upper()
            empty[""] = groc


        except EOFError:
            print("")
            break






