c = int(input())
d = int(input())
a = int(input())
b = int(input())
for y in range(c - 1, d + 1):
    if y >= c:
        print(y, end="\t")
    else:
        print("", end="\t")

    for x in range(a, b + 1):
        if y < c:
            print(x, end="\t")
        else:
            print(x * y, end="\t")
    print()
