# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        successor = None
        while root:
            print(successor)
            if p.val >= root.val:
                root = root.right
                
            else:
                successor = root
                root = root.left
                
        return successor
            
#         if p.right:
#             leftmost = p.right
#             while leftmost.left:
#                 leftmost = leftmost.left
            
#             self.successor = leftmost
#         else:
#             self.inordercase2(root, p)
            
#         return self.successor
        
#     def inordercase2(self, node, p):
        
#         if not node:
#             return
        
#         self.inordercase2(node.left, p)
#         if p == self.previous and not self.successor:
#             self.successor = node
#             return
        
#         self.previous = node
#         self.inordercase2(node.right, p)
        
        
                
        