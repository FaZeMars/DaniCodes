def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = int(dollars) * int(percent)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    nosign = d.replace("$", "")
    donei = float(nosign)





def percent_to_float(p):
    signo = p.replace("%", "")
    floati = float(signo)




main()

