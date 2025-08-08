class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        k=[]
        r=""
        for i in s:
            r+=i
            k.append(r)
        for i in words:
            if i in k:
                count+=1
        return count
            