f = input()
result = "wat?"
if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b +c) / 2
    result = (p * (p - a) * (p - b) * (p - c )) ** 0.5
elif f == 'прямоугольник':
    a = int(input())
    b = int(input())
    result = a * b
elif f == 'круг':
    r = int(input())
    result = 3.14 * r ** 2

print(result)