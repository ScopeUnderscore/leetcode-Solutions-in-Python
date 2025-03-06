class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=[]
        count=0
        while nums:
            res.append(nums.pop())
            count+=1
            res.sort()
            res=list(set(res[:k]))
            if res[:(k+1)]==list(range(1,k+1)):
                print(f"res:{res}")
                break
        return count