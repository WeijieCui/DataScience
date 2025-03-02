# You are given two 0-indexed integer arrays nums and multipliers of size n and 
# m respectively, where n >= m. 
# 
#  You begin with a score of 0. You want to perform exactly m operations. On 
# the iᵗʰ operation (0-indexed) you will: 
# 
#  
#  Choose one integer x from either the start or the end of the array nums. 
#  Add multipliers[i] * x to your score. 
#  
#  Note that multipliers[0] corresponds to the first operation, multipliers[1] 
# to the second operation, and so on. 
#  
#  Remove x from nums. 
#  
# 
#  Return the maximum score after performing m operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14. 
# 
#  Example 2: 
# 
#  
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# 
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  m == multipliers.length 
#  1 <= m <= 300 
#  m <= n <= 10⁵ 
#  -1000 <= nums[i], multipliers[i] <= 1000 
#  
# 
#  Related Topics Array Dynamic Programming 👍 2498 👎 508


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        ml = len(multipliers)
        nl = len(nums)
        graph = [[0] * (ml + 1) for _ in range(ml + 1)]
        for m in range(ml - 1, -1, -1):
            for l in range(m):
                r = nl - (m - l) + 1
                graph[m][l] = max(graph[m + 1][l + 1] + nums[l] * multipliers[m],
                                  graph[m + 1][l] + nums[r] * multipliers[m])
        return graph[0][0]
        # cache = {}
        # def np(s, l):
        #     key = (s, l)
        #     if key in cache:
        #         return cache[key]
        #     r = nl - (s - l) - 1
        #     if s == ml - 1:
        #         best = max(nums[l] * multipliers[s],
        #                    nums[r] * multipliers[s])
        #     else:
        #         best = max(nums[l] * multipliers[s] + np(s + 1, l + 1),
        #                    nums[r] * multipliers[s] + np(s + 1, l))
        #     cache.setdefault(key, best)
        #     return best
        #
        # return np(0, 0)

        # np = [[0] * (ml + 1) for _ in range(ml + 1)]
        # for o in range(ml, -1, -1):
        #     for l in range(2 ** (o + 1)):
        #         np[o, l] = multipliers[o] * nums[] + max(np[o + 1][l * 2], np[o + 1][l * 2 + 1])
        #


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumScore([1, 2, 3, 4], [3, 2, 1]))
