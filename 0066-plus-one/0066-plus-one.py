class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        j=[]
        for i in digits:
            res+=str(i)
        k=str(int(res)+1)
        for i in k:
            j.append(int(i))
        
        return j

