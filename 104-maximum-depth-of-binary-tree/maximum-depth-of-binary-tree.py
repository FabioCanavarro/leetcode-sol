# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def travel(node):
            if node == None:
                return 0

            le = travel(node.left)
            re = travel(node.right)

            if le > re:
                return le + 1
            else:
                return re + 1
        
        return travel(root)