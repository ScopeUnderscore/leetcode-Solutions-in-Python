class Solution:
    def isValid(self, s: str) -> bool:
        # brute force approach
        # while "()" in s or "{}" in s or "[]" in s:
        #     s=s.replace("()","").replace("{}","").replace("[]","")
        # return s==""
        #######################################################

        mapping={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in mapping:
                k  = stack.pop() if stack else '#'
                if mapping[i]!=k:
                    return False
            else:
                stack.append(i)
        return not stack