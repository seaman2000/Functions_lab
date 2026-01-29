def prices(product, count):

    if product == "coffee":
        price = 1.50
        return price * count
    elif product == "water":
        price = 1.00
        return price * count
    elif product == "coke":
        price = 1.40
        return price * count
    elif product == "snacks":
        price = 2.00
        return price * count


product_ = input()
count_ = int(input())

result = prices(product_, count_)
print(f"{result:.2f}")