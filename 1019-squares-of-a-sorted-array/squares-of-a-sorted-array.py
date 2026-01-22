class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] < nums[r] * nums[r]:
                res.append(nums[r] * nums[r])
                # decrement the right pointer
                r -= 1
            else:
                res.append(nums[l]* nums[l])
                # increment the left pointer
                l += 1
        return res[::-1] # retunr res array in reverse order
# Time Complexity: O(n) because we did this within one pass of the array
# Space Complexity: O(n) becuase we have an array to store our new result