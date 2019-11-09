import sys
import json
line = sys.stdin.readline().strip()
graph = json.loads(line)
while graph:
    hasdel = False
    for key in graph.keys():
        indegree = 0
        for k in graph.keys():
            if key in graph[k]:
                indegree += 1
        if indegree == 0:
            hasdel = True
            del graph[key]
    if not hasdel: break
print False if graph else True
