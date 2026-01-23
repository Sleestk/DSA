class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left pointer initalized at zero
        l = 0
        # right pointer iterates through the entire array
        for r in range(len(nums)):
            # if right pointer value is non zero
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums