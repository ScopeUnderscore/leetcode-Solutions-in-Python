class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lis=[]
        for i in list(set(nums)):
            if nums.count(i)>1:
                lis.append(i)
        return lis
        