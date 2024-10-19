class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count=0
        for m,i in enumerate(nums1):
            for n,j in enumerate(nums2):
                print(m,i)
                if i%(j*k)==0:
                    count+=1 
        return count
        