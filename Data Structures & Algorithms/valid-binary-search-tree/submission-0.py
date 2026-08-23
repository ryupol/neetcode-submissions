# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        stack = [(root, False)]
        checked = -1000000001

        while stack:
            node, visited = stack.pop()

            if visited:
                if checked >= node.val:
                    return False
                else:
                    checked = node.val
                

            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

        return True
