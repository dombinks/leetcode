# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        self.prev = -100001
        self.diff = 100001

        def search(node: TreeNode | None) -> int:
            if node.left:
                search(node.left)

            self.diff = min(self.diff, node.val - self.prev)
            self.prev = node.val

            if node.right:
                search(node.right)
                
            return self.diff

        return search(root)
