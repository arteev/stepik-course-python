sign_correction = {
    'север': [0, 1],
    'запад': [-1, 0],
    'юг': [0, -1],
    'восток': [1, 0],
}
actions = [input() for _ in range(int(input()))]
point = [0, 0]

for a in actions:
    action = a.split()
    dir = action[0]
    length = int(action[1])
    point[0] += length * sign_correction[dir][0]
    point[1] += length * sign_correction[dir][1]

print(*point)