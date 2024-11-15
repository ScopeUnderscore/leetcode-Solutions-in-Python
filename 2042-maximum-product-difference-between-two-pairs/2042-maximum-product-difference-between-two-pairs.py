class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest=max(nums)
        nums.remove(largest)
        second_l = max(nums)
        smallest = min(nums)
        nums.remove(smallest)
        second_s = min(nums)
        return (largest*second_l - smallest*second_s)
