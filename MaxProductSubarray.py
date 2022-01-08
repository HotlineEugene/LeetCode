class Solution:
    def maxProduct(self, A: List[int]) -> int:
        # Calculate prefix product in A.
        # Calculate suffix product in A.
        # Return the max of them.
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A), max(B))
