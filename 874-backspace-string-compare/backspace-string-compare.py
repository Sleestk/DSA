class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # start the two pointers at the end of the string
        i, j = len(s) - 1, len(t) - 1
        # makes sure that each pointer goes through each string no matter if one poitner goes out of bounds 
        while i >= 0 or j >= 0:
            # we must check each string individually, to remove char before "#", to make sure the strings match
            # count the number of backspaces for string s
            backspace_s = 0
            while i >= 0:
                if s[i] == "#":
                    backspace_s += 1
                    # decrement our pointer
                    i -= 1
                # reset our backspace_s for more than one # next to each other
                elif backspace_s > 0:
                    backspace_s -= 1
                    i -= 1
                else:
                    break
            # count the number of backspaces for string t
            backspace_t = 0
            while j >= 0:
                if t[j] == "#":
                    backspace_t += 1
                    # decrement our pointer
                    j -= 1
                # reset our backspace_s for more than one # next to each other
                elif backspace_t > 0:
                    backspace_t -= 1
                    j -= 1
                else:
                    break
            
            # compare the characters
            # if one string is different we know it is false
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            # if lengths are different they are not the same, return false
            if (i >= 0) != (j >= 0):
                return False
            
            # i and j must match now or be empty strings
            i -= 1
            j -= 1
        return True
# Time Complexity: O(n) since we itterate through the array once/touch every character once
# Space Complexity: O(1) since we do not use extra memory 