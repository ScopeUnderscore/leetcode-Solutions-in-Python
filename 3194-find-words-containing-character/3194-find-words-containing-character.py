class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for i,j in enumerate(words):
            if x in j:
                res.append(i)
        return res

        