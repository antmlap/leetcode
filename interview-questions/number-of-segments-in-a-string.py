class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        if s == "":
            return 0
        # Split string by spaces and count non-empty segments
        return len(s.split())

