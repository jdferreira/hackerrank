import itertools
from collections import Counter

n, num_pairs = [int(i) for i in input().split()]

classes = {i: {i} for i in range(n)}

for _ in range(num_pairs):
    pair = [int(i) for i in input().split()]
    class_0 = classes[pair[0]]
    class_1 = classes[pair[1]]
    the_class = class_0 | class_1
    for i in the_class:
        classes[i] = the_class

sets = dict((id(i), i) for i in classes.values())
length_counts = Counter(len(i) for i in sets.values())

result = 0
while length_counts:
    length, count = length_counts.popitem()
    result += length * count * sum(i * j for i, j in length_counts.items())
    if count > 1:
        result += length * length * count * (count - 1) // 2
print(result)
