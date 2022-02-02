class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1, l2 = len(s), len(p)
        if l1 < l2:
            return []

        res = []
        arr1, arr2 = [0] * 27, [0] * 27
        for i in range(l2):
            if i < l2 - 1:
                arr1[ord(s[i]) - 97] += 1
            arr2[ord(p[i]) - 97] += 1
        for i in range(l1 - l2 + 1):
            arr1[ord(s[i + l2 - 1]) - 97] += 1
            if arr1 == arr2:
                res.append(i)
            arr1[ord(s[i]) - 97] -= 1
        return res
