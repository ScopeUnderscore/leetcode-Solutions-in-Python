class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lis=[]
        for i in arr:
            if arr.count(i)==1:
                lis.append(i)
        if (k)>len(lis):
            return ""
        return lis[k-1]
