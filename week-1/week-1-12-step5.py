a, b, c = int(input()), int(input()), int(input())
if a > b:
    b, a = a, b
if b > c:
    c, b = b, c
if a > b:
    b, a = a, b

print(c)
print(a)
print(b)
