class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        k=int(num)
        while num[-1]=="0":
            k=k//10
            num=str(k)
        return num
        
    