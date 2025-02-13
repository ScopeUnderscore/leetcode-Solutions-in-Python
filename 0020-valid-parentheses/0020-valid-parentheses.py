class Solution:
    def isValid(self, s: str) -> bool:
        # brute force approach
        while "()" in s or "{}" in s or "[]" in s:
            s=s.replace("()","").replace("{}","").replace("[]","")
        return s==""
        