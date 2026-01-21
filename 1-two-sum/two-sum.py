class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if O(n) Time complexity then we need to creat a hashmap
        hashSet = {} # Gives the index : value
        for i in range(len(nums)): # Gives our indicies
            currNum = nums[i]
            comp = target - currNum
            if comp in hashSet:
                return [hashSet[comp], i]
            hashSet[currNum] = i
# Time Complexity: O(n) because hash map for constant time lookups
# Space Complexity: O(n) because space to store previous seen numbers