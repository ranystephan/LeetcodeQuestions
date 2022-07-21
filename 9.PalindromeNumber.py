#Easy



class Solution(object):
    def is Palindrome(self, x):
        
        S = str(x)

        for i in range (len(S)):
            if S[i] == S[-i -1]:
            continue
        else:
            return False

        return True
