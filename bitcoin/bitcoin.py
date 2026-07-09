import sys
import requests
import json

url = "rest.coincap.io/v3/assets/bitcoin?apiKey=d4d29d2d0a72c79a3448eceb57525d79b56c9d5b687793b4ddbb9dad86095625"
def main():

    try:
        response = requests.get(url)
        o = response.json()
        bitcoin = 0
        for dato in o["data"]:
            bitcoin = float(dato["priceUsd"])
            return bitcoin

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Conection Error")

    

