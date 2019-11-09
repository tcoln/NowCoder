import sys 
import collections
n = input()
table = []
for i in range(n):
    a = sys.stdin.readline().strip().split()
    table.append((a[0], a[1]))
keys = {}
newk = {}
for i in range(n):
    for j in range(n):
        if table[i][0] != table[j][0] and table[i][1] == table[j][1]:
            if (table[i][0], table[j][0]) not in keys:
                keys[(table[i][0], table[j][0])] = {table[i][1]}
            else:
                if table[i][1] not in keys[(table[i][0], table[j][0])]:
                    keys[(table[i][0], table[j][0])].add(table[i][1])
larger = []
for key in keys.keys():
    lens = len(keys[key])
    if lens > 2:
        larger.append((key[0], key[1], lens))
larger.sort(key=lambda item:item[0]+item[1])
for t in larger:
    print t[0],t[1],t[2]

