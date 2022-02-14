class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return (
            0
            if not root
            else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        )
