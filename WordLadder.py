class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
            len(beginWord) != len(endWord)
            or not beginWord
            or not endWord
            or not wordList
        ):
            return 0
        l = len(beginWord)
        dic = defaultdict(list)
        for word in wordList:
            if len(word) != l:
                continue
            for i in range(l):
                dic[word[:i] + "*" + word[i + 1 :]].append(word)

        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        while queue:
            curr, dis = queue.pop(0)
            for i in range(l):
                temp = curr[:i] + "*" + curr[i + 1 :]
                for nextWord in dic[temp]:
                    if nextWord not in visited:
                        if nextWord == endWord:
                            return dis + 1
                        queue.append((nextWord, dis + 1))
                        visited.add(nextWord)
        return 0
