# Given an array of strings words, return the first palindromic string in the
# array. If there is no such string, return an empty string "".
#
#  A string is palindromic if it reads the same forward and backward.
#
#
#  Example 1:
#
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
#
#
#  Example 2:
#
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
#
#
#  Example 3:
#
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is
# returned.
#
#
#
#  Constraints:
#
#
#  1 <= words.length <= 100
#  1 <= words[i].length <= 100
#  words[i] consists only of lowercase English letters.
#
#
#  Related Topics Array Two Pointers String 👍 1543 👎 55


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[::-1] == word:
                return word
        return ''

# leetcode submit region end(Prohibit modification and deletion)
