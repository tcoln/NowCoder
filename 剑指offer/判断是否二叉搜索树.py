# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here        
        
        def recusiveVerify(sequence):
            l = len(sequence)
	    if l == 0 or l == 1:
		return True
            i = 0
            while(i < l and sequence[i] < sequence[-1]):
                i += 1
            j = i
            while(j < l and sequence[j] > sequence[-1]):
                j += 1
	    #print sequence, i, j, l
            if j == l - 1:
                ans = recusiveVerify(sequence[:i]) and recusiveVerify(sequence[i:-1])
                return ans
            else:
                return False
        
	if len(sequence) == 0:
		return False    
        #print  recusiveVerify(sequence)
        return recusiveVerify(sequence)

s = Solution()
s.VerifySquenceOfBST([4,8,6,12,16,14,10])
s.VerifySquenceOfBST([4,6,7,5])
