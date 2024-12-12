class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x= max(nums)
        m=0
        for _ in range(k):
            m+=x
            x=x+1
        print(m)
        return m

        