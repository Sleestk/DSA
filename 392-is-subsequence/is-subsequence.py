class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        # run a while loop for the pointer going out of bounds
        while i < len(s) and j < len(t):
            # two condition that we need to meet
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
# Time Complexity: O(n) since we iterate through the array once
# Space Complexity: O(1) since we do not use extra memory
