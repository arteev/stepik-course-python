heights = dict.fromkeys(range(1, 12))
with open("dataset.txt") as file:
    for line in file:
        pupil = line.strip().split('\t')
        key = int(pupil[0])
        heights_class = heights[key]
        if heights_class is None:
            heights_class = [0, 0]
        heights_class[0] += int(pupil[2])
        heights_class[1] += 1
        heights[key] = heights_class
for i in range(1, 12):
    heights_class = heights[i]
    if heights_class is None:
        print(i, "-")
    else:
        print(i, heights_class[0] / heights_class[1])
