# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        def descend(node: TreeNode | None, path: int) -> int:
            if node:
                path ^= (1 << node.val)
    
                if (not node.left) and (not node.right):
                    return 1 if path & (path - 1) == 0 else 0
    
                return descend(node.left, path) + descend(node.right, path)
            return 0

        return descend(root, 0)
