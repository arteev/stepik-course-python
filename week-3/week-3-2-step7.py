d = dict()
for x in [int(input()) for x in range(int(input()))]:
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])
