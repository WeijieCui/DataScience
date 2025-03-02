# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#  An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
#
#
#  Example 1:
#  Input: s = "anagram", t = "nagaram"
# Output: true
#
#  Example 2:
#  Input: s = "rat", t = "car"
# Output: false
#
#
#  Constraints:
#
#
#  1 <= s.length, t.length <= 5 * 10⁴
#  s and t consist of lowercase English letters.
#
#
#
#  Follow up: What if the inputs contain Unicode characters? How would you
# adapt your solution to such a case?
#
#  Related Topics Hash Table String Sorting 👍 12070 👎 399


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap.setdefault(c, 1)
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                tmap.setdefault(c, 1)
        for k, v1 in smap.items():
            if k not in tmap:
                return False
            v2 = tmap.pop(k)
            if v1 != v2:
                return False
        return not tmap
# leetcode submit region end(Prohibit modification and deletion)
