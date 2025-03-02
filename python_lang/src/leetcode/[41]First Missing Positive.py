# Given an unsorted integer array nums. Return the smallest positive integer 
# that is not present in nums. 
# 
#  You must implement an algorithm that runs in O(n) time and uses O(1) 
# auxiliary space. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  Related Topics Array Hash Table 👍 16623 👎 1834


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] < len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(1, len(nums) + 1):
            if nums[i - 1] != i:
                return i
        return len(nums) + 1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    for nums, expected in [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([-1, 4, 2, 1, 9, 10], 3),
        ([1, 1], 2),
    ]:
        result = solution.firstMissingPositive(nums)
        if result != expected:
            print(f'nums={nums} expected={expected} result={result}')
