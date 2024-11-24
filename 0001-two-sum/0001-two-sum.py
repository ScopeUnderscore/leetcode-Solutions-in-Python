class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in temp and temp.index(diff) != i:
                return [temp.index(diff), i]
            else:
                temp.append(nums[i])
