class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic={}
        # for i in range(len(arr)):
        #     for j in range(0,len(arr)):
        #         print(i,j)
        #         if i!=j and arr[i] == 2*arr[j]:
        #             return True
        # return False   

        for i in range(len(arr)):
            if arr[i] * 2 in dic or arr[i]/2 in dic:
                return True
            dic[arr[i]]=0
        return False
                
                
                
            
        