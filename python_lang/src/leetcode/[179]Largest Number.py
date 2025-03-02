# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
#
#  Since the result may be very large, so you need to return a string instead
# of an integer.
#
#
#  Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
#  Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 100
#  0 <= nums[i] <= 10⁹
#
#
#  Related Topics Array String Greedy Sorting 👍 8004 👎 663
from functools import cmp_to_key
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2) -> int:
            return 1 if n1 + n2 > n2 + n1 else -1

        nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        return '0' if nums[0] == '0' else ''.join(str(n) for n in nums)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3, 2, 6]))
    print(s.largestNumber([0, 0, 0]))
    print(s.largestNumber([99, 98130299, 981303]))
