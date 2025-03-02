# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics Array Dynamic Programming 👍 12640 👎 433


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numbers = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, len(numbers)):
            for j in range(1, len(numbers[i]) - 1):
                numbers[i][j] = numbers[i - 1][j - 1] + numbers[i - 1][j]
        return numbers

# leetcode submit region end(Prohibit modification and deletion)
