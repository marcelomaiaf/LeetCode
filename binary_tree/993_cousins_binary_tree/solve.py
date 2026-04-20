# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        pair_depth = []
        def dfs(node, depth, parent):
            if not node:
                return 
            if node.val == x:
                pair_depth.append((depth, parent))
            if node.val == y:
                pair_depth.append((depth, parent))

            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)

        dfs(root, 0, 0)
        return pair_depth[0][0] == pair_depth[1][0] and pair_depth[0][1] != pair_depth[1][1]
        