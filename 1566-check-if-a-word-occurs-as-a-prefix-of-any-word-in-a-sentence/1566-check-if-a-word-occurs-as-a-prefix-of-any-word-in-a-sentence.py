class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count =0
        k=sentence.split(" ")
        for i in k:
            if i.startswith(searchWord):
                return k.index(i) + 1
        return -1



        
    
        