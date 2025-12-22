import requests
import sys
import decimal

try:
    while True:
        try:
            if len(sys.argv) == 1:
                sys.exit("Missing command-line argument")

            n = decimal.Decimal(sys.argv[1])

            info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=95b6d87f2d225428f862a470f77e25a736a273bd49949272e83c1c52f5ac0dc1")

            info = info.json()
            usd_price = decimal.Decimal(info["data"]["priceUsd"])

            total_price = usd_price * n

            print(f"$ {total_price:,.4f}")
            sys.exit()
        except IndexError:
            pass
    
except decimal.InvalidOperation:
    sys.exit("Command-line argument is not a numeber")