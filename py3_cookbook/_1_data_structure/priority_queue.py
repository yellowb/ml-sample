import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0

    def _push(self, priority, item):
        heapq.heappush(self._queue,
                       (-priority, self._count, item))  # the first two elements in tuple are to be compared.
        self._count = self._count + 1

    def push(self, item):
        self._push(item.price, item)

    def pop(self):
        return heapq.heappop(self._queue)[2]

    def size(self):
        return len(self._queue)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return 'name = %s, price = %s' % (self.name, self.price)


item_1 = Item('Apple', 10)
item_2 = Item('Orange', 6)
item_3 = Item('Banana', 3)
item_4 = Item('Pig', 30)
item_5 = Item('Chicken', 25)

# order by price from high to low
pq = PriorityQueue()
pq.push(item_1)
pq.push(item_2)
pq.push(item_3)
pq.push(item_4)
pq.push(item_5)

for i in range(pq.size()):
    print(pq.pop())
