class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=sorted(s)
        j=sorted(t)
        return k==j
        
        
        
        