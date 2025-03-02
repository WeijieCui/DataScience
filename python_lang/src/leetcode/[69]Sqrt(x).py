# Given a non-negative integer x, return the square root of x rounded down to 
# the nearest integer. The returned integer should be non-negative as well. 
# 
#  You must not use any built-in exponent function or operator. 
# 
#  
#  For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down 
# to the nearest integer, 2 is returned.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 8030 👎 4475


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 0
        high = x
        last = None
        while True:
            root = int((low + high) / 2)
            if root == last:
                return root
            root2 = root ** 2
            if root2 == x:
                return root
            elif root2 > x:
                high = root
            else:
                low = root
            last = root

# leetcode submit region end(Prohibit modification and deletion)
