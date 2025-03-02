# Given an integer array nums where every element appears three times except 
# for one, which appears exactly once. Find the single element and return it. 
# 
#  You must implement a solution with a linear runtime complexity and use only 
# constant extra space. 
# 
#  
#  Example 1: 
#  Input: nums = [2,2,3,2]
# Output: 3
#  
#  Example 2: 
#  Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  Each element in nums appears exactly three times except for one element 
# which appears once. 
#  
# 
#  Related Topics Array Bit Manipulation 👍 7757 👎 682


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map.setdefault(n, 1)
        return [k for k, v in num_map.items() if v == 1][0]
# leetcode submit region end(Prohibit modification and deletion)
