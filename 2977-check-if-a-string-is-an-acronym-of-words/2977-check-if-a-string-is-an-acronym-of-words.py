class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        k=""
        for i in words:
            k+=i[0]
        print(k)
        return k==s
        