class Solution:
    def exist(self, board, word):
        l1 = len(board)
        l2 = len(board[0])
        for i in range(l1):
            for j in range(l2):
                if word[0]== board[i][j]:
                    if self.search(board, word, i, j):
                        return True
        return False

    def search(self, board, word,r,c, i=0):
        if i == len(word):
            return True
        if r >= len(board) or r < 0:
            return False
        if c >= len(board[0]) or c < 0:
            return False
        if word[i] != board[r][c]:
            return False

        board[r][c] = '*'
        result = self.search(board,word,r+1, c, i+1) or self.search(board, word, r-1, c, i + 1) or \
                 self.search(board, word, r, c+1, i + 1) or self.search(board, word, r, c-1, i+1)
        board[r][c] = word[i]
        return result

board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word= "ABCCED"
print(word)
result = Solution()
print(result.exist(board, word))
word = "ABCB"
print(word)
result = Solution()
print(result.exist(board, word))


