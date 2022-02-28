price = [1, 2, 3, 1, 2]


for i in price:
    k = price.index(max(price))
    if i < k:
        pass
    elif i > 2:
        price = price[k:]
        k = price.index(max(price))

    print(k)
