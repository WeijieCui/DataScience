# Given a string s which represents an expression, evaluate this expression and
# return its value.
#
#  The integer division should truncate toward zero.
#
#  You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2³¹, 2³¹ - 1].
#
#  Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
#  Example 1:
#  Input: s = "3+2*2"
# Output: 7
#
#  Example 2:
#  Input: s = " 3/2 "
# Output: 1
#
#  Example 3:
#  Input: s = " 3+5 / 2 "
# Output: 5
#
#
#  Constraints:
#
#
#  1 <= s.length <= 3 * 10⁵
#  s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
#  s represents a valid expression.
#  All the integers in the expression are non-negative integers in the range [0,
#  2³¹ - 1].
#  The answer is guaranteed to fit in a 32-bit integer.
#
#
#  Related Topics Math String Stack 👍 6123 👎 838


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '', -1)
        nums = []
        signs = []
        n1 = ''
        multi = False
        devise = False
        for c in s:
            if c == '+':
                if multi:
                    nums[-1] *= int(n1)
                    multi = False
                elif devise:
                    nums[-1] = int(nums[-1] / int(n1))
                    devise = False
                else:
                    nums.append(int(n1))
                n1 = ''
                signs.append(1)
            elif c == '-':
                if multi:
                    nums[-1] *= int(n1)
                    multi = False
                elif devise:
                    nums[-1] = int(nums[-1] / int(n1))
                    devise = False
                else:
                    nums.append(int(n1))
                n1 = ''
                signs.append(-1)
            elif c == '*':
                if multi:
                    nums[-1] *= int(n1)
                elif devise:
                    nums[-1] = int(nums[-1] / int(n1))
                    devise = False
                else:
                    nums.append(int(n1))
                multi = True
                n1 = ''
            elif c == '/':
                if multi:
                    nums[-1] *= int(n1)
                    multi = False
                elif devise:
                    nums[-1] = int(nums[-1] / int(n1))
                else:
                    nums.append(int(n1))
                devise = True
                n1 = ''
            else:
                n1 += c
        if multi:
            nums[-1] *= int(n1)
        elif devise:
            nums[-1] = int(nums[-1] / int(n1))
        else:
            nums.append(int(n1))
        sums = nums[0] + sum(a * b for a, b in zip(nums[1:], signs))
        return sums


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate('3+2*0 +5*2-10 * 2'))
