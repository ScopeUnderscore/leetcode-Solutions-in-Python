class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:


        k=[]
        sorted_num=sorted(nums)
        lis = list(range(sorted_num[0],(sorted_num[-1]+1)))
        for i in lis:
            if i not in nums:
                k.append(i)
        if k is not None:
            return sorted(k)
        else:
            return []
            
        
        

                

                


        