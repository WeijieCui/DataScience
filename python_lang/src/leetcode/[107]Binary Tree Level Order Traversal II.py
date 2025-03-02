# Given the root of a binary tree, return the bottom-up level order traversal 
# of its nodes' values. (i.e., from left to right, level by level from leaf to root)
# . 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Breadth-First Search Binary Tree 👍 4820 👎 322


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = [root]
        values = []
        while nodes:
            next_nodes = []
            values.append([node.val for node in nodes])
            for node in nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            nodes = next_nodes
        return values[::-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(bool([]))
