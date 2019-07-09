#coding=utf-8
import sys
line = sys.stdin.readline().strip().split(' ')
n, m, c = int(line[0]), int(line[1]), int(line[2])
peals = []
for i in range(n):
    line = sys.stdin.readline().strip().split(' ')
    colorNums = int(line[0])
    colors = [int(line[j+1]) for j in range(colorNums)]
    peals.append(colors)

count = 0
conflictColors = set()
mColors = {}
for i in range(n):
    if i == 0:
        for j in range(m):
            row = i + j
            if row >= n:
                row  %= n
            colors = peals[row]
            for color in colors:
                if not mColors.has_key(color):
                    mColors[color] = 1
                else:
                    mColors[color] += 1 
                    if color not in conflictColors:
                        count += 1
                        conflictColors.add(color)
    else:
        colors = peals[i-1]
        for color in colors:
            mColors[color] -= 1 
        row = i + m -1
        if row >= n:
            row  %= n
        colors = peals[row]
        for color in colors:
            if not mColors.has_key(color):
                mColors[color] = 1
            else:
                mColors[color] += 1 
                # mColors[color]有键并且值有可能为0
                if mColors[color] > 1 and color not in conflictColors: 
                    count += 1
                    conflictColors.add(color)
print count
