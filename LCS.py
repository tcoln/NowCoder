# -*- coding:utf-8 -*-

class LCS:
    def findLCS(self, A, n, B, m):
        # write code here
        lcs = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        print lcs[n][m]
        return lcs[n][m]

if __name__ == '__main__':
	l = LCS()
	l.findLCS("zynnqufc",8,"ddbauhkw",8)
