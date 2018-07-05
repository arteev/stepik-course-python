d = dict()
for s in input().split():
    key = s.lower()
    d[key] = d.setdefault(key, 0) + 1

for key, value in d.items():
    print(key, value)
