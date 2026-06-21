def main():

    price = 50
    print("Amount due:", price)
    coin = int(input("insert coin"))
    owed = price - coin

    if coin in [25, 10, 5]:
         while owed > 0:
             print("Amount due:", owed)
             nueva_moneda = int(input("insert coin: "))
             if nueva_moneda in [25, 10, 5]:
                 owed = owed - nueva_moneda
             else:
                 print("insert a valid coin")

    if owed <= 0:
        print("Change due:", abs(owed))




main()
