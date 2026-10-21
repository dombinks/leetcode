# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def descend(node: TreeNode | None, num: int) -> int:
            if not node:
                return 0

            num = (num * 10) + node.val

            out = 0
            if node.left:
                out += descend(node.left, num)
            if node.right:
                out += descend(node.right, num)
            if not node.left and not node.right:
                out = num

            return out

        return descend(root, 0)
