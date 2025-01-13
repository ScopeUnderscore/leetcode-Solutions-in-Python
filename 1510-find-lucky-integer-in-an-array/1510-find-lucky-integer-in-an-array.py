class Solution:
    def findLucky(self, arr: List[int]) -> int:
        k=[]
        res={x:arr.count(x) for x in arr}
        for x,y in res.items():
            if x==y:
                k.append(x)
        print(k)
        
        if len(k)==1:
            return k[0]
        
        if len(k)>=2:
            return max(k)
        return -1


        