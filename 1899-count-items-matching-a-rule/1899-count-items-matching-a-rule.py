class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=="type":
            k=0
        elif ruleKey =="color":
            k=1
        elif ruleKey =="name":
            k=2
        
        for i in items:
            icount=0
            for j in i:
                # icount+=1
                print(j,i.index(j))
                if j == ruleValue and icount==k:
                    count+=1
                icount+=1
        return count
        