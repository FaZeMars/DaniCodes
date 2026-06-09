def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    nosign = d.replace("$", "")
    done = float(nosign)
    return done





def percent_to_float(p):
    signo = p.replace("%", "")
    casa = float(signo)
    resultado = (int(casa) / 100) * done
    return resultado



main()

