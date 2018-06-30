a = float(input())
b = float(input())
op = input()
calc = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: ("Деление на 0!" if b==0 else a / b),
    '*': lambda a, b: a * b,
    'mod': lambda a, b: ("Деление на 0!" if b==0 else a % b),
    'pow': lambda a, b: a ** b,
    'div': lambda a, b: ("Деление на 0!" if b==0 else a // b),
}
if op not in calc:
    print("Не корректная операция")
else:
    print(calc[op](a,b))
