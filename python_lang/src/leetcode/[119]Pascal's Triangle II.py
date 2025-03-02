# Given an integer rowIndex, return the rowIndexᵗʰ (0-indexed) row of the 
# Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
#  Follow up: Could you optimize your algorithm to use only O(rowIndex) extra 
# space? 
# 
#  Related Topics Array Dynamic Programming 👍 4774 👎 337


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            pre = nums[0]
            for j in range(1, i):
                current = nums[j]
                nums[j] += pre
                if j >= rowIndex:
                    break
                pre = current
        return nums

# leetcode submit region end(Prohibit modification and deletion)
