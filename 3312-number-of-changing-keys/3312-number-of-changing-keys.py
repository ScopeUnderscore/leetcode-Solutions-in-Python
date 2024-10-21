class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        l=2
        m=0
        s=s.lower()
        while l<(len(s)+1):
            k=s[m:l]
            print(m,l)
            if k[0]==k[1]:
                l+=1
                m+=1
            elif k[0]!=k[1]:
                count+=1
                l+=1
                m+=1
        return count    

        