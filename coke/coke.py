def main():

    price = 50
    print("Amount due:", price)
    coin = int(input("insert coin"))
    owed = price - coin

    if coin in [25, 10, 5]:
         while owed > 0:
             print("Amount due:", owed)
             nueva_moneda = int(input("insert coin: "))
             owed = owed - nueva_moneda
     else:
        print("Insert a valid coin")


    if owed <= 0:
        print("Change due:", abs(owed))




main()
