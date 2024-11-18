class Solution:
    def findGCD(self, nums: List[int]) -> int:
        for i in range(1,max(nums)+1):
            if max(nums)%i==0 and min(nums)%i==0:
                k=i
        return k
            

        