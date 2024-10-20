class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        lis=[]
        # new_i=""
        # for i in nums:
        #     k=list(str(i))
        #     for j in k:
        #         new_i+=str(max(k))
        #     lis.append(int(new_i))
        #     new_i=""
        # return sum(lis)

        for i in nums:
            numstr = str(i)
            max_val = max(numstr)
            newstr = max_val*len(numstr)
            lis.append(int(newstr))
        return sum(lis)





        