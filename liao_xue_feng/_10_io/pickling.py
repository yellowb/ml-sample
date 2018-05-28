# Sample of serialization


import pickle

L = list(x + 1 for x in range(100))
content = pickle.dumps(L)

with open('./data/serialization', 'wb') as output_file:
    pickle.dump(L, output_file)

print('dump done.')
