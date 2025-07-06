print("1-sum to usd")
print("2-usd to sum")

choice = input()

rate = 12500

if choice == "1":
    sums = float(input("sum: "))
    dollars = sums/rate
    print(sums, "sums is", dollars, "dollars")
elif choice == "2":
    dollars = float(input("dollars: "))
    sums = dollars*rate
    print(dollars, "dollars is", sums, "sums")
else:
    print("error")