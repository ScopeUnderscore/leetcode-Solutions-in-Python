class Solution:
    def isUgly(self, n: int) -> bool:
        prime_fact = [2,3,5]
        if n<=0:
            return False
        for i in prime_fact:
            print(i)
            while n%i==0:
                print (i)
                n=n//i
                print(n)

        if n==1:
            return True
        else:
            return False

            