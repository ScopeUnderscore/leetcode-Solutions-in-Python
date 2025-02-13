class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
            sum=0
        while any(i for i in grid):
            max_vals=[i.pop() for i in grid ]
            sum +=max(max_vals)
        return sum




        