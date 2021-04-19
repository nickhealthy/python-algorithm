# first solved
# def solution(nums):
#     sum = 0
#     pair = []
    
#     nums.sort()
#     for i in nums:
#         pair.append(i)
#         if len(pair) == 2:
#             sum += min(pair)
#             pair = []
    
#     return sum


# second solved
class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2]) 
