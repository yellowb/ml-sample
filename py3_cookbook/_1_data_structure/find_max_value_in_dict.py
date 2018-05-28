""" Sample to find the max/min value(and its key) from a dictionary """

# data
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Can not use `max` or `min` on dict because it takes action on the keys, not values.

# approach 1, use `zip()` to exchange the keys and values
price_to_stock = list(
    zip(prices.values(), prices.keys()))  # Note: the object returned by `zip()` can be iterated only once
print(price_to_stock)
print('Max price stock = ', max(price_to_stock))
print('Min price stock = ', min(price_to_stock))

# approach 2, pass a key function into `max` or `min`
print('Max price stock = ', max(prices, key=lambda k: prices[k]))
print('Min price stock = ', min(prices, key=lambda k: prices[k]))
