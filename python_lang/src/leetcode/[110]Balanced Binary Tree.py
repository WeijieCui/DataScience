# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 10691 👎 690


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        level_map = {None: 0}

        # calculate the level of each node
        def calculate(node: Optional[TreeNode]):
            # if the level of the node is already calculated, return it
            if node in level_map:
                return level_map[node]
            # if the node is None, the level is 0
            if not node:
                return 0
            # if the node is a leaf, the level is 1
            elif not node.left and not node.right:
                level = 1
            # if the node has children, the level is the maximum level of its children plus 1
            else:
                level = max(calculate(node.left), calculate(node.right)) + 1
            level_map.setdefault(node, level)
            return level

        # calculate the level of each node
        calculate(root)
        tolerance = (-1, 0, 1)

        # compare the level of the left child and the right child of each node
        def compare(node: Optional[TreeNode]):
            if not node:
                return True
            return (level_map[node.left] - level_map[node.right] in tolerance
                    and compare(node.left) and compare(node.right))

        return compare(root)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # Wrapped the test case in a function to prevent scope issues
    n41 = TreeNode(4)
    n42 = TreeNode(4)
    n31 = TreeNode(3, n41, n42)
    n32 = TreeNode(3)
    n21 = TreeNode(2, n31, n32)
    n22 = TreeNode(2)
    n1 = TreeNode(1, n21, n22)
    solution = Solution()
    print(solution.isBalanced(n1))
