class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        lenght = len(gas)
        i = 0
        while i < lenght:
            netsum = 0
            accept = True
            for j in range(i, i + lenght):
                idx = j % lenght
                netsum += gas[idx] - cost[idx]
                if netsum < 0:
                    i = j + 1
                    accept = False
                    break
            if accept:
                return i
        return -1
