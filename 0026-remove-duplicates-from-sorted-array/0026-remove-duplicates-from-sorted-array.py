class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique=set(nums)
        nums.clear()
        for i in unique:
            nums.append(i)
            nums.sort()
         

        return len(nums)
        