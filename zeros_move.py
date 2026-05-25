class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j =0
        for i in range(len(nums)):
            if nums[i]!=0: # j is park non zero nos and i scans every element
                nums[j]= nums[i]
                j=j+1
        for i in range(j,len(nums)):
            nums[i]=0