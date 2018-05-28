from collections import OrderedDict
import json

d1 = OrderedDict()
d1['apple'] = 1
d1['orange'] = 2
d1['banana'] = 3
d1['chicken'] = 4

for k, v in d1.items():
    print(k, v)

print(json.dumps(d1))
