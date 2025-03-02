# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
# 
#  Related Topics Math Dynamic Programming Memoization 👍 21626 👎 809


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(step: int):
            if step <= 2:
                return step
            if step in cache:
                return cache[step]
            num = climb(step - 1) + climb(step - 2)
            cache.setdefault(step, num)
            return num

        for i in range(n):
            climb(i)
        return climb(n)
# leetcode submit region end(Prohibit modification and deletion)
