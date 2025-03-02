# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
#  Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
#  Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
#  Constraints:
#
#
#  3 <= nums.length <= 3000
#  -10⁵ <= nums[i] <= 10⁵
#
#
#  Related Topics Array Two Pointers Sorting 👍 30408 👎 2819


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        m = {}
        for i, n in enumerate(nums):
            if n in m:
                m[n].append(i)
            else:
                m.setdefault(n, [i])
        unis = [n for n in m.keys()]
        idx_map = {n: i for i, n in enumerate(unis)}
        for i, ni in enumerate(unis):
            # triple same elements
            if ni == 0 and len(m[ni]) >= 3:
                solutions.append([ni, ni, ni])
            # double same elements
            if ni != 0 and len(m[ni]) >= 2 and -2 * ni in m:
                solutions.append([ni, ni, -2 * ni])
            # three different elements
            for j, nj in enumerate(unis[i + 1:]):
                nk = -ni - nj
                if nk != ni and nk != nj and nk in m and idx_map[nk] > j + i + 1:
                    solutions.append([ni, nj, nk])
        return solutions

# leetcode submit region end(Prohibit modification and deletion)
