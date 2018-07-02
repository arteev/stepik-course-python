m = list()
while True:
    a = input()
    if a == "end":
        break
    m.append([int(i) for i in a.split()])
r = [[0 for j in range(len(m[0]))] for i in range(len(m))]

for i in range(len(r)):
    for j in range(len(r[i])):
        p = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
        for pc in p:
            piy = pc[0]
            pix = pc[1]
            if pix >= len(r[i]): pix = 0
            if pix < 0: pix = -1
            if piy >= len(r): piy = 0
            if piy < 0: piy = -1
            r[i][j] += m[piy][pix]

for i in range(len(r)):
    for j in range(len(r[i])):
        print(r[i][j], end=" ")
    print()
