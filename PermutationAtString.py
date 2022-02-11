class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s2_len < s1_len:
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for c in s1:
            s1_count[ord(c) - ord("a")] += 1
        print(s1_count)

        for i in range(len(s2)):
            s2_count[ord(s2[i]) - ord("a")] += 1

            if i >= s1_len:
                s2_count[ord(s2[i - s1_len]) - ord("a")] -= 1

            if s1_count == s2_count:
                return True
        return False
