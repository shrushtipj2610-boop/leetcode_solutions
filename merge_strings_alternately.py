class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        j=0
        result =[]
        while i<len(word1) and j<len(word2):
             result.append(word1[i])
             result.append(word2[j])
             i=i+1
             j=j+1
        if i<len(word1):
            result.append(word1[i:])
        if j<len(word2):
            result.append(word2[j:])
        
        return "".join(result)  