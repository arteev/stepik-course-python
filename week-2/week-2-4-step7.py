dna = input()
out = ""
oldc = dna[0]
countc = 0
for c in dna:
    if oldc != c:
        if countc != 0:
            out += oldc + str(countc)
        oldc = c
        countc = 1
    else:
        countc += 1
else:
    out += oldc + str(countc)

print(out)
