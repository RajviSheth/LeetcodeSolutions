# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursive(curr_node):
            if not curr_node:
                return False
            
            left = recursive(curr_node.left)
            
            right = recursive(curr_node.right)
            
            mid = curr_node == p or curr_node == q
            
            if mid + left + right >= 2:
                self.ans = curr_node
                
            return mid or left or right
        
        recursive(root)
        return self.ans
        