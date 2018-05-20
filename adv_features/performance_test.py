import time as time

# #2 & #3 are fast , #1 is slow

amount = 1000 * 1000 * 200

t1 = time.time()

list1 = list(range(amount))[::2]

print('Time consumption of list(range(amount))[::2] = ', time.time() - t1)

t2 = time.time()

list2 = list(range(amount)[::2])

print('Time consumption of list(range(amount)[::2]) = ', time.time() - t2)

t3 = time.time()

list3 = list(range(0, amount, 2))

print('Time consumption of list(range(0, amount, 2)) = ', time.time() - t3)
