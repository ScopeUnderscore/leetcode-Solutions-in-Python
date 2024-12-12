class Solution:
    def minimumSum(self, num: int) -> int:
        k=list(str(num))
        k.sort()
        return int(k[0]+k[-1])+int(k[1]+k[2])
        

        