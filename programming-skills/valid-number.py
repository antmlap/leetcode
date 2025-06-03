class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            left, right = s.split('.', 1)
            if not left and not right:
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True

        # split by e or E
        if 'e' in s or 'E' in s:
            parts = s.lower().split('e')
            if len(parts) != 2:
                return False
            base, exp = parts
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        else:
            return isInteger(s) or isDecimal(s)

