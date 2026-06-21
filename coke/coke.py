def main():

    price = 50
    print("Amount due:", price)
    coin = int(input("insert coin"))
    owed = price - coin

    while owed > 0:
        print("Amount due:", owed)
        nueva_moneda = int(input("insert coin: "))
        owed = owed - nueva_moneda

    if owed <= 0:
        print("Change due: ", owed.replace("-", ""))




main()



