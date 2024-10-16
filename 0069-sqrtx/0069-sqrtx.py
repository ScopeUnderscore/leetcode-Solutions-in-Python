class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x

        if x==0:
            return x

        while low<=high:
            guess = (low+high)//2
            if guess**2 == x:
                return guess

            elif guess**2 < x:
                low=guess+1
            
            else:
                high=guess-1
        
        return high


            