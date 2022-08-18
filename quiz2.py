cost_price = int(input("enter the price of bike "))

if cost_price > 100000:
    tax = 15/ 100 * cost_price
    print(tax)

elif cost_price > 50000:
    tax = 0.1 * cost_price
    print(tax)

elif cost_price < 50000:
    tax = 5/100 * cost_price
    print(tax)

else:
    print("not valid")

