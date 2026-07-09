import sys
import requests
import json

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=d4d29d2d0a72c79a3448eceb57525d79b56c9d5b687793b4ddbb9dad86095625"
def main():
    try:
        x = float((sys.argv[1].strip()))
    except (ValueError, IndexError):
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(url)
        o = response.json()
        bitcoin = 0
        for dato in o["data"]:
            bitcoin = dato[float("priceUsd")]
            return bitcoin
    except requests.RequestException:
        sys.exit("Conection Error")

    total = x * bitcoin
    print(f"${total:,.4f}")



main()
