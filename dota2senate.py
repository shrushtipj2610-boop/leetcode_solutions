class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       n= len(senate) 
       radiant= deque()
       dire= deque()
       for i,s in enumerate(senate): #i in positon and s is character
        if s=='R':
            radiant.append(i)
        else:
            dire.append(i)
       while radiant and dire:
            r= radiant.popleft()
            d=dire.popleft()
            if r<d:
                radiant.append(r+n)
            else:
                dire.append(d+n)
       return "Radiant" if radiant else "Dire"