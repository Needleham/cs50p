'''
    In a file called bitcoin.py, implement a program that:
    Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy.
    If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

    Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. 
    You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, 
    among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

    import requests

    try:
    ...
    except requests.RequestException:
    ...
    Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

'''


# API KEY - 24d217b51f0dd68a77eae62ed34c868683f7029761f61a81e31c7768b26696b6
import sys
import requests

try:
    bitcoins = float(sys.argv[1])
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=24d217b51f0dd68a77eae62ed34c868683f7029761f61a81e31c7768b26696b6')
    data = r.json()
    amount = float(data["data"]["priceUsd"]) * bitcoins

    print(f"${amount:,.4f}")
except (requests.RequestException, IndexError, ValueError):
    sys.exit("Invalid Argument")


