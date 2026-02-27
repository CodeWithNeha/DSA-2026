# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
li = []
class Solution:
    def inorderTraversal(self, root):
        li = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            li.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return li
        