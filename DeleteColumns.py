class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        remove = 0
        for x in range(len(strs[0])):
            temp = [s[x] for s in strs]
            if temp != sorted(temp):
                remove += 1
        return remove
