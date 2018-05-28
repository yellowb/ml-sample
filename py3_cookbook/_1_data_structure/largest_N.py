""" How to find the largest N elements from input """

import heapq

# for numbers
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# for complex types
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, portfolio, key=lambda x: x['price']))
print(heapq.nsmallest(3, portfolio, key=lambda x: x['price']))

# sequence input
h = [1, 3, 5, 7, 9]
heapq.heapify(h)
print(h)
heapq.heappush(h, 4)
heapq.heappush(h, 0)
print(h)
print(heapq.nlargest(3, h))
print(heapq.nsmallest(3, h))

