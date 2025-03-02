# Given two binary strings a and b, return their sum as a binary string. 
# 
#  
#  Example 1: 
#  Input: a = "11", b = "1"
# Output: "100"
#  
#  Example 2: 
#  Input: a = "1010", b = "1011"
# Output: "10101"
#  
#  
#  Constraints: 
# 
#  
#  1 <= a.length, b.length <= 10⁴ 
#  a and b consist only of '0' or '1' characters. 
#  Each string does not contain leading zeros except for the zero itself. 
#  
# 
#  Related Topics Math String Bit Manipulation Simulation 👍 9299 👎 956


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(a)
        print(b)
        if len(a) > len(b):
            a, b = b, a
        nums = [0] * len(b)
        bias = len(b) - len(a)
        addition = 0
        for i in range(len(a) - 1, -1, -1):
            cp = addition
            if a[i] == '1' and b[i + bias] == '1':
                nums[i + bias] = addition
                addition = 1
            elif a[i] == '1' or b[i + bias] == '1':
                nums[i + bias] = (addition + 1) % 2
                addition = 1 if addition == 1 else 0
            else:
                nums[i + bias] = addition
                addition = 0
            print(a[i], b[i + bias], cp, addition, nums[i + bias])
        print(nums)
        print('b')
        for i in range(len(b) - len(a) - 1, -1, -1):
            print(b[i])
            if b[i] == '1':
                nums[i] = (addition + 1) % 2
                addition = 1 if addition == 1 else 0
            else:
                nums[i] = addition
                addition = 0
        if addition:
            nums.insert(0, 1)
        print(nums)
        nums = ''.join(str(n) for n in nums)
        print(nums)
        return nums


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()

    print(solution.addBinary('100', '110010'))
