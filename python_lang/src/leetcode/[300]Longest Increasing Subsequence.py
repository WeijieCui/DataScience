# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
#
#  Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
#  Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
#  Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 2500
#  -10⁴ <= nums[i] <= 10⁴
#
#
#
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#  Related Topics Array Binary Search Dynamic Programming 👍 20775 👎 436


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic problem
        # dp[m] = max(dp[0]...dp[m-1]) + 1 (if nums[i] < nums[m])
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = max([dp[j] for j in range(i) if nums[j] < nums[i]] + [0]) + 1
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)
