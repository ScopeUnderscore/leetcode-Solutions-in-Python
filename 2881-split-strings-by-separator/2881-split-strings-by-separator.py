class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res =""
        for word in words:
            res+=word
            res+=separator
        print(res)
        return res.replace(separator," ").split()
       

            
        