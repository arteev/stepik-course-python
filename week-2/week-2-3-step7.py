a, b = int(input()), int(input())
s = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        s += i
print(s / count)
