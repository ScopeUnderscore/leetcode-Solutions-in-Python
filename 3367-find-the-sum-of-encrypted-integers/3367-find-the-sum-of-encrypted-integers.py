class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        lis=[]
        new_i=""
        for i in nums:
            k=list(str(i))
            for j in k:
                new_i+=str(max(k))
            lis.append(int(new_i))
            new_i=""
            print(lis)
        return sum(lis)


        