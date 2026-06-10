def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    pre = d.replace("$", "")
    done = float(pre)
    return done

def percent_to_float(p):
    pres = p.replace("%", "")
    casa = float(pres)
    resultado = (int(casa) / 100)
    return resultado


main()



