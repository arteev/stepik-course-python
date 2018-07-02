s = 0
digits = []
while s != 0 or len(digits) == 0:
    d = int(input())
    digits.append(d)
    s += d
print(sum([d ** 2 for d in digits]))
