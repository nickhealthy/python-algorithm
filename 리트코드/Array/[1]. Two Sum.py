class Solution:            
    def twoSum(self, nums, target):
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = idx

        for i in range(len(nums)):
            if target - nums[i] in nums_map and i != nums_map[target - nums[i]]:
                return [i, nums_map[target - nums[i]]]
