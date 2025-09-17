class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in index and index[ch]>=left:
                left = index[ch] + 1
            index[ch] = right
            max_len = max(max_len, right-left+1)
        return max_len
        