from collections_py import Counter
'''babu = Counter("venkatesh babu")
print(babu)'''#Counter({'e': 2, 'a': 2, 'b': 2, 'v': 1, 'n': 1, 'k': 1, 't': 1, 's': 1, 'h': 1, ' ': 1, 'u': 1})
'''venky =Counter("veenkatesh babu").most_common()
print(venky)'''#[('e', 3), ('a', 2), ('b', 2), ('v', 1), ('n', 1), ('k', 1), ('t', 1), ('s', 1), ('h', 1), (' ', 1), ('u', 1)]
'''babu = Counter("venkatesh babu")
print(list(babu.elements()))'''#['v', 'e', 'e', 'n', 'k', 'a', 'a', 't', 's', 'h', ' ', 'b', 'b', 'u']

from collections_py import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)  #defaultdict(<class 'list'>, {'yellow': [1, 3], 'red': [1], 'blue': [2, 4]})
d.items()








