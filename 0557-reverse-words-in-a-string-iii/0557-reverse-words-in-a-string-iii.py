class Solution:
    def reverseWords(self, s: str) -> str:
        lis1=[]
        lis=s.split(" ")
        for i in lis:
            lis1.append(i[::-1])

        return " ".join(lis1)
        