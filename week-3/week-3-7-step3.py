dic = set([input().lower() for _ in range(int(input()))])
text = set()
for y in [x.split() for x in [input() for _ in range(int(input()))]]:
    text.update(y)
printed = set()
for word in text:
    if word.lower() not in dic and word.lower() not in printed:
        print(word)
        printed.add(word)
