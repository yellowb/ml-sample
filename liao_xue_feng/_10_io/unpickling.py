# Sample of de-serialization


import pickle

with open('./data/serialization', 'rb') as source_file:
    L = pickle.load(source_file)
    print(L)

print('load done.')
