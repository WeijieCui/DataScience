# Given an m x n grid of characters board and a string word, return true if 
# word exists in the grid. 
# 
#  The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter 
# cell may not be used more than once. 
# 
#  
#  Example 1: 
#  
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCCED"
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "SEE"
# Output: true
#  
# 
#  Example 3: 
#  
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCB"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board and word consists of only lowercase and uppercase English letters. 
#  
# 
#  
#  Follow up: Could you use search pruning to make your solution faster with a 
# larger board? 
# 
#  Related Topics Array String Backtracking Matrix 👍 15671 👎 657
# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        q = queue.Queue()
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j]:
                    q.put([(i, j)])
        if len(word) == 1:
            return not q.empty()
        while not q.empty():
            path = q.get()
            # print(path)
            steps = set(s for s in path)
            i, j = path[-1]
            idx = len(steps)
            options = [(x, y) for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)) if
                       0 <= x < r and 0 <= y < c and (x, y) not in steps and board[x][y] == word[idx]]
            if len(options) > 0 and idx >= len(word) - 1:
                return True
            for op in options:
                cp = [s for s in path]
                cp.append(op)
                q.put(cp)
        return False

# leetcode submit region end(Prohibit modification and deletion)
