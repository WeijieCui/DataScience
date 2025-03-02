# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
#  Example 1:
#  Input: s = "leetcode"
# Output: 0
#
#  Example 2:
#  Input: s = "loveleetcode"
# Output: 2
#
#  Example 3:
#  Input: s = "aabb"
# Output: -1
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁵
#  s consists of only lowercase English letters.
#
#
#  Related Topics Hash Table String Queue Counting 👍 8948 👎 293


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap = {}
        for i, c in enumerate(s):
            if c in smap:
                smap[c][1] += 1
            else:
                smap.setdefault(c, [i, 1])
        non_repeat = [(c, i) for c, (i, count) in smap.items() if count == 1]
        return min(non_repeat, key=lambda i: i[1])[1] if non_repeat else -1
# leetcode submit region end(Prohibit modification and deletion)
