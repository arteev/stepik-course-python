d = dict()
with open('dataset.txt', 'r') as fin:
    for line in fin:
        for s in line.strip().lower().split():
            d[s] = d.setdefault(s, 0) + 1
value_max = d[max(d, key=lambda key: d[key])]
print(min([k for k, v in d.items() if v == value_max]), value_max)
