import requests
import sys
import json


def main():
    coinURL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:

        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        amountBTC = sys.argv[1]

        if amountBTCi.isdecimal == False:
            sys.exit("Command-line argument is not a number")


        r = requests.get(coinURL)
        #print(json.dumps(r.json(), indent=2))
        btcDict = r.json()
        bpiDict = btcDict["bpi"]
        usdDict = bpiDict["USD"]
        currentPrice = usdDict["rate_float"]

        value = float(currentPrice) * float(amountBTC)
        value = float(value)

        #for i in usdDict:
        #    print(f"{i }   {usdDict[i]}")

        #print(f"Current BTC price in USD: {currentPrice}")
        #value =
        #print(f$"{currentPrice:,.4}) * int(amountBTC))

        print(f"${value:,}")






    except requests.RequestException:
        sys.exit("Error")


def check(ammount):
    ammount = str(ammount)
    ammount.isdigit()


if __name__ == "__main__":
    main()