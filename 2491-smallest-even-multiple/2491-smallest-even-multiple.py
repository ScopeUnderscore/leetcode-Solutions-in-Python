class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res =[]
        for i in range(1,(2*n)+1):
            if i%2==0 and i%n==0:
                res.append(i)
        return min(res)


        