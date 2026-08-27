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
        
        vals = []
        counts = [k]
        def inorder(node):
            if not node:
                return None

            if counts[0] <= 0:
                return None
                
            inorder(node.left)

            if counts[0] > 0:
                vals.append(node.val)
                counts[0] -= 1

            inorder(node.right)

        inorder(root)
        return vals[-1] if len(vals) > 0 else 0