import sys
import bisect
if __name__ == "__main__":    
    line = sys.stdin.readline().strip().split(' ')
    n, m = int(line[0]), int(line[1])
    query = {}
    for nn in range(n):
        line = sys.stdin.readline().strip().split(' ')
        a, b, c, d = int(line[0]), line[1], int(line[2]), line[3]
        if not query.has_key(c):
            query[c] = [(a, b, c, d)]
        else:
            query[c].append((a, b, c, d))
    for mm in range(m):
        line = sys.stdin.readline().strip().split(' ')
        ad, cx = int(line[0]), int(line[1])
        count = 0
        if not query.has_key(cx):
            print 0
        else:
            queryc = query[cx]
            for qc in queryc: # find y ~~ qc
                for key in query.keys():
                    if key != cx:
                        items = query[key]
                        for item in items:
                            if abs(qc[0]-item[0])<=ad and qc[1] == item[1] and qc[2] != item[2] and qc[3] != item[3]:
                                count += 1
            print count 
