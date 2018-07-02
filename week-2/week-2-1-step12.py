a = int(input())
b = int(input())
if a > b:
    b, a = a, b

i = 0
nok = 0
while not nok:
    if i % a == 0 and i % b == 0:
        nok = i
    i += 1
print(nok)
