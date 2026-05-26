class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       i=0
       j=0
       while i<len(t) and j<len(s):
        if s[j]== t[i]:
            j=j+1
        i=i+1
       if j == len(s): # reached at last of s so all s characters are matched
            return True
       else:
            return False