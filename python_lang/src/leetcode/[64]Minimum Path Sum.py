# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
#  Note: You can only move either down or right at any point in time.
#
#
#  Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
#  Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
#  Constraints:
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 200
#
#
#  Related Topics Array Dynamic Programming Matrix 👍 12354 👎 168
# leetcode submit region begin(Prohibit modification and deletion)
import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[sys.maxsize] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # top row
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # other rows
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
