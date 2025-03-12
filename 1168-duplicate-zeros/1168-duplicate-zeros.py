class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr1=[]
        for i in range(len(arr)):
            if arr[i]==0:
                arr1.append(arr[i])
                arr1.append(arr[i])
            
                
            else:
                arr1.append(arr[i])

        print(arr1)
        for i in range(len(arr)):
            if i<=len(arr):
                arr.insert(i,arr1[i])
                arr.pop()
       
            
        
        

        

    



         