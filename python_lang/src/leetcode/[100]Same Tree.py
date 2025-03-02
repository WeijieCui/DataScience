# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
#  
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
#  
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 11
# 373 👎 236
# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        nodes = queue.Queue()
        nodes.put((p, q))
        while not nodes.empty():
            a, b = nodes.get()
            if (a is None and b is not None) or (a is not None and b is None):
                return False
            else:
                if a.val != b.val:
                    return False
                if a.left is None or b.left is None:
                   if (a.left is None and b.left is not None) or (a.left is not None and b.left is None):
                       return False
                else:
                    nodes.put((a.left, b.left))
                if a.right is None or b.right is None:
                   if (a.right is None and b.right is not None) or (a.right is not None and b.right is None):
                       return False
                else:
                    nodes.put((a.right, b.right))
        return True

# leetcode submit region end(Prohibit modification and deletion)
