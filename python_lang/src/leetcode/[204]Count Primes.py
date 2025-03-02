# Given an integer n, return the number of prime numbers that are strictly less 
# than n. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 0
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: n = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 5 * 10⁶ 
#  
# 
#  Related Topics Array Math Enumeration Number Theory 👍 7829 👎 1428
import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_primes = [0, 0] + [1] * (n - 2)
        # print(is_primes)
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_primes[i] != 0:
                for j in range(i ** 2, n, i):
                    is_primes[j] = 0
        # print(is_primes)
        return sum(is_primes)

# leetcode submit region end(Prohibit modification and deletion)
