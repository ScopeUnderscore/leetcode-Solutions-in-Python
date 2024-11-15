class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lis=[]
        for i in range(len(nums)):
            k=sum(nums[:i+1])
            lis.append(k)
        return lis
            

        