class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list1=[x for grid1 in grid for x in grid1]
        list2=[]
        for i in list1:
            if list1.count(i)>1 and i not in list2:
                list2.append(i)
        for j in range(1,len(grid)**2+1):
            if j not in list1:
                list2.append(j) 
        return list2
                    
                
        