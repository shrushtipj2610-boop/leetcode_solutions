class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i=0
        result=[]
        a= max(candies)
        for i in range(len(candies)):
         if candies[i] + extraCandies>=a:
          result.append(True)
         else:
          result.append(False)
        return result
