avg_math, avg_ru, avg_phy = 0.0, 0.0, 0.0
count = 0

with open('file_out.txt', 'w') as fout:
    with open('dataset.txt', 'r') as fin:
        for line in fin:
            for s in line.strip().lower().split():
                data = s.split(";")
                count += 1
                avg = sum(int(x) for x in data[1:]) / 3
                avg_math += int(data[1])
                avg_phy += int(data[2])
                avg_ru += int(data[3])
                fout.write(str(avg))
                fout.write('\n')

    fout.writelines(str(avg_math / count) + " " + str(avg_phy / count) + " " + str(avg_ru / count))
