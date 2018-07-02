a = [int(i) for i in input().split()]
a.sort()
out = []
cur = None
for c in a:
    if cur != c:
        if a.count(c) > 1:
            print(c, end=" ")
        cur = c
