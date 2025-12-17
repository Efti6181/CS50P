import sys
import requests

# Check if user provided exactly 1 command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Check if command-line argument is a number
try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# CoinCap API endpoint
url = "https://rest.coincap.io/v3/assets/bitcoin"

# 🔥 REPLACE ONLY THE TEXT BELOW WITH YOUR API KEY
# Example format: "Bearer 7330c7fcfdd90b6a123456789abcdef"
headers = {
    "Authorization": "Bearer 7330c7fcfdd90b6a8b2c68c17415a664b9ae1a680c5f4806233895920db1e83b"
}

# Fetch Bitcoin price safely
try:
    response = requests.get(url, headers=headers)
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()

# Print the total cost with commas + 4 decimal places
print(f"${amount * price:,.4f}")
