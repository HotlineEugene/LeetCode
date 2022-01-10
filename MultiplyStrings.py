class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_to_int = dict()
        for i in range(10):
            str_to_int[str(i)] = i
        int_num1, int_num2 = 0, 0
        for i in num1:
            int_num1 = int_num1 * 10 + str_to_int[i]
        for i in num2:
            int_num2 = int_num2 * 10 + str_to_int[i]
        return str(int_num1 * int_num2)
