# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁵]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 72
# 21 👎 1297


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d = 0
        next_q = [root]
        while True:
            d += 1
            cur_q = next_q
            next_q = []
            for node in cur_q:
                if node.left is None and node.right is None:
                    return d
                if node.left is not None:
                    next_q.append(node.left)
                if node.right is not None:
                    next_q.append(node.right)

# leetcode submit region end(Prohibit modification and deletion)
