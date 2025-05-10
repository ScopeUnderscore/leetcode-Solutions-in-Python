class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1)
        b=set(nums2)
        k= list(a.intersection(b))
        print(k)
        if k:
            return min(k)
        else:
            return -1