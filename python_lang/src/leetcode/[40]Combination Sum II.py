# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics Array Backtracking 👍 10281 👎 288


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cmap = {}
        for c in candidates:
            if c in cmap:
                cmap[c] += 1
            else:
                cmap.setdefault(c, 1)
        candidates = sorted((c for c in set(candidates)), reverse=True)
        print(cmap)
        print(candidates)

        def combine(idx: int, t: int) -> [[int]]:
            combinations = []
            val = candidates[idx]
            for i in range(cmap.get(candidates[idx]) + 1):
                rest = t - val * i
                sub_combinations = combine(idx + 1, rest) if idx < len(candidates) - 1 and rest >= candidates[
                    -1] else []
                if i > 0:
                    for sub_combination in sub_combinations:
                        sub_combination.extend([val] * i)
                    if rest == 0:
                        sub_combinations.append([val] * i)
                combinations.extend(sub_combinations)
            return combinations

        return combine(0, target)

# leetcode submit region end(Prohibit modification and deletion)
