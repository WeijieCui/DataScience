# Given an integer array nums, find a subarray that has the largest product, 
# and return the product. 
# 
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
#  
# 
#  Related Topics Array Dynamic Programming 👍 18252 👎 602


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total_max_p = nums[0]
        max_p = nums[0]
        min_p = nums[0]
        for n in nums[1:]:
            tmp_max_p = max(n, max_p * n, min_p * n)
            min_p = min(n, max_p * n, min_p * n)
            max_p = tmp_max_p
            total_max_p = max(max_p, total_max_p)
        return total_max_p


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
