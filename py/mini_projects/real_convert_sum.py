import urllib.request as ur
from urllib import request
import json

url = "https://api.exchangerate-api.com/v4/latest/USD"

print("1-sum to usd")
print("2-usd to sum")

choice = input()

with ur.urlopen(url) as response:
        data = json.loads(response.read().decode())
        rate = data['rates']['UZS']
        # print(f"1 USD = {rate} UZS")

# rate = 12500

if choice == "1":
    sums = float(input("sum: "))
    dollars = sums/rate
    print("{:,.0f}".format(int(sums)), "sums is", 
          "{:,.0f}".format(int(dollars)), "dollars")
elif choice == "2":
    dollars = float(input("dollars: "))
    sums = dollars*rate
    print("{:,.0f}".format(int(dollars)), "dollars is", 
          "{:,.0f}".format(int(sums)), "sums")
else:
    print("error")
