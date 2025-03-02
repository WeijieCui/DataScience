# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#  Example 2:
#  Input: nums = [1], k = 1
# Output: [1]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  k is in the range [1, the number of unique elements in the array].
#  It is guaranteed that the answer is unique.
#
#
#
#  Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority
# Queue) Bucket Sort Counting Quickselect 👍 17240 👎 658


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for n in nums:
            if n not in mp:
                mp.setdefault(n, 1)
            else:
                mp[n] += 1
        counts = [(k, v) for k, v in mp.items()]
        counts.sort(key=lambda i: i[1], reverse=True)
        return [k for k, v in counts[:k]]

# leetcode submit region end(Prohibit modification and deletion)
