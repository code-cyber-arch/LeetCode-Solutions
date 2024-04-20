# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)  # Visit left subtree
            result.append(node.val)     # Visit node itself
            inorder(node.right, result) # Visit right subtree

        result = []
        inorder(root, result)
        return result
