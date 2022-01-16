class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_filled_seat = -1
        max_len = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if last_filled_seat == -1:
                    max_len = i
                    last_filled_seat = i

                else:
                    max_len = max(max_len, ((i - last_filled_seat) // 2))
                    last_filled_seat = i

        last_pos = len(seats) - 1
        max_len = max(max_len, (last_pos - last_filled_seat))
        return max_len
