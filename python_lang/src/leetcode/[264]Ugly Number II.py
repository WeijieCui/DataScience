# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
#  Given an integer n, return the nᵗʰ ugly number.
#
#
#  Example 1:
#
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
# ugly numbers.
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
#
#  Constraints:
#
#
#  1 <= n <= 1690
#
#
#  Related Topics Hash Table Math Dynamic Programming Heap (Priority Queue) 👍 5
# 951 👎 316


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n
        # initiate 3 queues for number 2,3,5
        q2 = deque()
        q3 = deque()
        q5 = deque()
        q2.extend((4, 5, 6))
        q3.extend((3, 4, 5, 6))
        q5.extend((2, 3, 4, 5, 6))
        current = 6
        idx = 6
        # calculate ugly numbers one by one
        while idx < n:
            # pop next possible factor
            n2 = q2.popleft()
            n3 = q3.popleft()
            n5 = q5.popleft()
            # calculate next possible ugly numbers
            n22 = n2 * 2
            n33 = n3 * 3
            n55 = n5 * 5
            # compare and find the min ugly numbers
            if n22 <= n33 and n22 <= n55:
                current = n22
                if n22 != n33:
                    q3.appendleft(n3)
                if n22 != n55:
                    q5.appendleft(n5)
            elif n33 < n22 and n33 <= n55:
                current = n33
                q2.appendleft(n2)
                if n33 != n55:
                    q5.appendleft(n5)
            else:
                current = n55
                q2.appendleft(n2)
                q3.appendleft(n3)
            # put the ugly numbers in queues
            q2.append(current)
            q3.append(current)
            q5.append(current)
            idx += 1
        return current
# leetcode submit region end(Prohibit modification and deletion)
