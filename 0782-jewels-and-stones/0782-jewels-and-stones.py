class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum=0
        for i in jewels:
            print(i)
            # if i in list(stones)
            sum=sum+list(stones).count(i)
            print(sum)

        return sum
        
