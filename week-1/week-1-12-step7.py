num = int(input())
a = num % 1000
b = num // 1000
if a // 100 + (a % 100 // 10) + a % 10 == b // 100 + (b % 100 // 10) + b % 10:
    print("Счастливый")
else:
    print("Обычный")
