class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i,j in enumerate(nums):

            k=len(set(nums[:i+1]))-len(set(nums[i+1:]))
            res.append(k)
        return res

        