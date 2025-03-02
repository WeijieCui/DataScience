# Given a string s, reverse only all the vowels in the string and return it.
#
#  The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# lower and upper cases, more than once.
#
#
#  Example 1:
#  Input: s = "hello"
# Output: "holle"
#
#  Example 2:
#  Input: s = "leetcode"
# Output: "leotcede"
#
#
#  Constraints:
#
#
#  1 <= s.length <= 3 * 10⁵
#  s consist of printable ASCII characters.
#
#
#  Related Topics Two Pointers String 👍 4534 👎 2780


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = [c for c in s]
        left = 0
        right = len(ls) - 1
        while left < right:
            while left < right and ls[left] not in 'aeiouAEIOU':
                left += 1
            while left < right and ls[right] not in 'aeiouAEIOU':
                right -= 1
            if left < right and ls[left] in 'aeiouAEIOU' and ls[right] in 'aeiouAEIOU':
                ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1
        return ''.join(ls)
# leetcode submit region end(Prohibit modification and deletion)
