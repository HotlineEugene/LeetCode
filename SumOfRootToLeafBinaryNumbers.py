# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        return self.findSum(root, "", ans)

    def findSum(self, root, temp, ans):
        if root is None:
            return 0
        temp += str(root.val)

        if root.left is None and root.right is None:
            ans += int(temp, 2)
            return ans

        return self.findSum(root.left, temp, ans) + self.findSum(root.right, temp, ans)
