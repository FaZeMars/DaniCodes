def main():

    price = 50
    print("Amount Due:", price)
    coin = int(input("Inser Coin: "))
    if coin in [25, 10, 5]:
        owed = price - coin
    else:
        owed = price

    while owed > 0:
        print("Amount Due:", owed)
        nueva_moneda = int(input("Insert Coin: "))
        if nueva_moneda in [25, 10, 5]:
            owed = owed - nueva_moneda
        else:
            print("insert a valid coin")

    if owed <= 0:
        print("Change due:", abs(owed))




main()
