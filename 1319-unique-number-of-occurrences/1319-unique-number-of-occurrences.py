class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] =1
        # print(freq.values())
        # print(freq)
        occurance=list(freq.values())

        return len(occurance)==len(set(occurance))