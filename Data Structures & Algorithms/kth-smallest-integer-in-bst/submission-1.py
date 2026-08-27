# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k == 0:
            return 0
        
        res = 0
        counts = k
        def inorder(node):
            nonlocal res, counts

            if not node:
                return None

            if counts <= 0:
                return None
                
            inorder(node.left)

            if counts > 0:
                res = node.val
                counts -= 1

            inorder(node.right)

        inorder(root)
        return res