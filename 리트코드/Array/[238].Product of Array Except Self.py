class Solution:
    def productExceptSelf(self, nums):
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i] # 1, 2, 6, 24
            print(p)
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
            print(nums[i])
