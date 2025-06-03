class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # Check if there is at least one duplicate character
            return len(set(s)) < len(s)

        # Find all positions where s and goal differ
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]

        # To be buddy strings, there must be exactly 2 differences and they must swap to match
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

