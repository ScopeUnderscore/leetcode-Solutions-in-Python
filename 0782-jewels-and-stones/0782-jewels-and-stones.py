class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum=0
        for i in jewels:
            sum=sum+list(stones).count(i)
        return sum
        
