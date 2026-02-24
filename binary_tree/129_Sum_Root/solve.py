# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def rec(root, n: str):
            if not root:
                return 0
            n += str(root.val)

            if not root.left and not root.right:
                return int(n)

            return rec(root.left, n) + rec(root.right, n)
        
        return rec(root, "")
            
        