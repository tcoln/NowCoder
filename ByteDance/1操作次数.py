import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    ops = 0
    while (N != 1):
        p = pow(N,0.5)
        intp = int(p)
        if intp == p:
            N = p
            ops += 1
        else:
            ops += N - intp**2
            N = intp**2
	#print N, p, ops
    print int(ops)
