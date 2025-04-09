class Solution:
    def distinctIntegers(self, n: int) -> int:
        board=[n]
        for i in board:
            for j in range(1,i+1):
                if i%j==1:
                    board.append(j)
        return len(set(board))

        