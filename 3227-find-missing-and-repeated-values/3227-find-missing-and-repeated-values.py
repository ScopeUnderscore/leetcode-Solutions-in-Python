class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        k=[]
        dic={}
        res=[]
        for i in grid:
            if isinstance(i,list):
                k+=i
        print(set(k))
        for i in range(len(k)):
            dic[k[i]]= dic.get(k[i],0)+1

        for key, val in dic.items():
            if val==2:
                res.append(key)

       



        # for j in range(1,len(k)+1):
        #     if j in set(k):
        #         res.append(j)
        # print(res)

        for h in range(1,len(k)+1):
            if h not in k:
                res.append(h)
        return res

    