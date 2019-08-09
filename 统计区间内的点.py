import sys
import bisect

if __name__ == "__main__":    
    T = int(sys.stdin.readline().strip())
    ans = 0
    for t in range(T):
        line = sys.stdin.readline().strip().split(' ')
        n, m = int(line[0]), int(line[1])
        a = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        a.sort() 
        print 'Case #' + str(t+1) + ':'
        for j in range(m):
            ans = 0
            line = sys.stdin.readline().strip().split(' ')
            l, r = int(line[0]), int(line[1])
            ll = bisect.bisect_left(a, l)
            rr = bisect.bisect_right(a, r)
            if l > a[-1] or r < a[0]:
                print 0
            else:
                print rr - ll

