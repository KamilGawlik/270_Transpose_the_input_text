adding = True
stringtable = []
while adding:
    x = input()
    if x == " ":
        adding = False
        continue
    stringtable.append(x)
    if stringtable[-1] == "": stringtable.pop()

maxlenght = len(stringtable[0])
for x in stringtable:
    if len(x) > maxlenght:
        maxlenght = len(x)

for x in range(0, len(stringtable)):
    if len(stringtable[x]) < maxlenght:
        S = stringtable[x] + ' ' * (maxlenght-len(stringtable[x]))
        stringtable[x] = S

for x in range(0,maxlenght):
    for row in stringtable:
        print(row[x],' ', end='')
    print("")

