# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
#  Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i + j]
# where:
#
#
#  0 <= j <= nums[i] and
#  i + j < n
#
#
#  Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 1000
#  It's guaranteed that you can reach nums[n - 1].
#
#
#  Related Topics Array Dynamic Programming Greedy 👍 14411 👎 568
# leetcode submit region begin(Prohibit modification and deletion)
import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        length = len(nums)
        jumps = [sys.maxsize] * length
        jumps[0] = 0
        span = 0
        for i, n in enumerate(nums):
            if n > span:
                for j in range(1, n + 1):
                    if i + j < length and jumps[i + j] > jumps[i] + 1:
                        jumps[i + j] = jumps[i] + 1
        return jumps[-1]
# leetcode submit region end(Prohibit modification and deletion)
