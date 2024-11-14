class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=list(s)
        j=list(t)
        k.sort()
        j.sort()
        if str(k)==str(j):
            return True

        else:
            return False
        
        
        