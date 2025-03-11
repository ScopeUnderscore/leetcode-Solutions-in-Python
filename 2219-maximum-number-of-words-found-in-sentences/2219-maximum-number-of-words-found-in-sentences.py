class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=[]
        for i in sentences:
            res.append(i.count(" "))
        print(res)
        return max(res)+1


        