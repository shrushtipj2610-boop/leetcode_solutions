class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1= set(word1)
        set2= set(word2)
        count1= Counter(word1)  #{a:1} example 2 
        count2= Counter(word2) #{a:2,} ex 2
        if set1== set2 and sorted(count1.values())== sorted(count2.values()):
            return True
        else:
            return False