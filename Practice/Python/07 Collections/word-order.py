from collections import Counter

n = int(input())
seen = set()
l = []
c = Counter()

for _ in range(n):
    word = input()
    if word not in seen:
        l.append(word)
        seen.add(word)
    c[word] += 1

print(len(c))
print(' '.join(str(c[i]) for i in l))
