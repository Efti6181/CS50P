import sys
import requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {
    "Authorization": "Bearer 7330c7fcfdd90b6a8b2c68c17415a664b9ae1a680c5f4806233895920db1e83b"
}
try:
    response = requests.get(url, headers=headers)
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()
print(f"${amount * price:,.4f}")

