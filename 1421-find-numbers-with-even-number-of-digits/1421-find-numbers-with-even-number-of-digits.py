class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k=[len(str(x)) for x in nums if len(str(x)) %2==0]
        return len(k)



        