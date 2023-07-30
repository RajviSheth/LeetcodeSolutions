# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
            
#         max_path = -float('inf')
#         def gain_from_subtree(node):
#             nonlocal max_path
#             if not node:
#                 return 0
            
#             gain_from_left = max(gain_from_subtree(node.left), 0)
#             gain_from_right = max(gain_from_subtree(node.right), 0)
            
#             max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            
#             return max(gain_from_left + node.val, gain_from_right + node.val)
        
        
#         gain_from_subtree(root)
#         return max_path
    