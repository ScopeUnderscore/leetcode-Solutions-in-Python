class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        k=n//20
        arr.sort()
        return sum(arr[k:(n-k)])/(n-2*k)

        