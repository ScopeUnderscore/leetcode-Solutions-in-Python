class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i!=j and arr[i] == 2 * arr[j]:
        #             return True
        # return False
        dic = {}
        for i in arr:
            if i * 2 in dic or  i/2 in dic :
                return True
            dic[i]=0
        return False
        