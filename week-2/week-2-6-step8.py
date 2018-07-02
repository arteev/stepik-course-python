c = int(input())
k = 0
for i in range(c + 1):
    for j in range(i):
        k += 1
        if k > c:
            exit(0)
        print(i, end=" ")
