class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Whitespace

        if not s:
            return 0

        sign = 1
        i = 0

        # 2. Sign check
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        # 3. Conversion
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # 4. Rounding
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

