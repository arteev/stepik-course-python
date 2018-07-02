n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
k = n
p = 0
for i in range(n // 2 + 1):
    c = n - k
    for lr in range(k):
        p += 1
        m[i][lr + c // 2] = p

    for rb in range(i + 1, k + c // 2):
        p += 1
        m[rb][n - c // 2 - 1] = p

    for bl in range(n - c // 2 - 2, c // 2 - 1, -1):
        p += 1
        m[-(i + 1)][bl] = p

    for lt in range(n - i - 2, i, -1):
        p += 1
        m[lt][c // 2] = p
    k -= 2

for i in m: print(*i)