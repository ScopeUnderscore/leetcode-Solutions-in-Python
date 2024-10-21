class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        lis=[]
        for i in nums:
            if nums.count(i) > 2:
                lis.append("False")

            elif nums.count(i) <2:
                lis.append("True")
        if "False" in lis:
            return False
        else:
            return True 
        


            
