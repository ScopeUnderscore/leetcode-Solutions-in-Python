class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic=dict(zip(heights,names))
        lis=[]
        k=list(dic.keys())
        k.sort(reverse=True)
        for i in k:
            lis.append(dic[i])
        return lis

