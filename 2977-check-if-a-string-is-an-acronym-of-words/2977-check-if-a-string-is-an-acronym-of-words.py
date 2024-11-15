class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        k=""
        for i in words:
            k=k+i[0]
            j=k[:len(words)]
        print(s[:len(words)])
        return j==s



                
                