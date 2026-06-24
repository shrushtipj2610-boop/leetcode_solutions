class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2= set(nums2)
        answer1, answer2=[],[]
        for i in set1:
            if i not in set2:
                answer1.append(i) # in set we don't need to i=i+1 as set moves the index by itself
        for i in set2:
            if i not in set1:
                answer2.append(i)
        return[answer1,answer2]