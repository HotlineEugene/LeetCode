class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, maxi = deque([[root, 0]]), 0
        while len(q):
            maxi = max(maxi, q[-1][1] - q[0][1] + 1)
            for i in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append([node.left, 2 * pos + 0])
                if node.right:
                    q.append([node.right, 2 * pos + 1])
        return maxi
