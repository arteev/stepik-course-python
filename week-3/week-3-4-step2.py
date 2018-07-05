def decode(data):
    prev = None
    c = ""
    out_data = ""
    for d in data:
        if d.isnumeric():
            c += d
            continue
        if prev != d:
            if c != "":
                out_data += prev * int(c)
                c = ""
            prev = d
    if c != "":
        out_data += prev * int(c)
    return out_data


with open('file_out.txt', 'w') as fout:
    with open('file.txt', 'r') as fin:
        for line in fin:
            line = line.strip()
            fout.writelines(decode(line) + '\n')
