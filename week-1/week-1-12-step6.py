count = int(input())
end = ""
mod = count % 10

if mod in [0, 5, 6, 7, 8, 9] or 11 < count <= 20 or (count % 100 in [11, 12, 13, 14]):
    end = "ов"
elif mod in [2, 3, 4]:
    end = "а"

print(count, "программист" + end)
