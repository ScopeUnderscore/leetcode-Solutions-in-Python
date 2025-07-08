class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        result  = {}
        for i in arr:
            result[i] =result.get(i, 0) + 1
        print(result)
        occurance = list(result.values())

        return len(occurance) == len(set(occurance)) 