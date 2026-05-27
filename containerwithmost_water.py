class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right= len(height)-1
        maxwater=0
        while left<right:
            water= (right-left)* min(height[left],height[right])
            maxwater= max(maxwater,water)
            if height[left]<height[right]:
                left= left+1
            else:
                right=right-1

        return maxwater