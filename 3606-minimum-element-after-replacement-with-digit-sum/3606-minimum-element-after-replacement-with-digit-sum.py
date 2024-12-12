class Solution:
    def minElement(self, nums: List[int]) -> int:
        val=[]
        for i in nums:
            sum=0
            for k in str(i):
                sum+=int(k)
            val.append(sum)
        return min(val)
        


        