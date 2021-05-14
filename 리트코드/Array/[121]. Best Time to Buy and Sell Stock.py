# first solved - 브루트포스
# class Solution:
#     def maxProfit(self, prices):
#         max_price = 0
#         for i, price in enumerate(prices):
#             for j in range(i+1, len(prices)):
#                 max_price = max(prices[j] - price, max_price)
#         return max_price

import sys

# second solved - 카데인 알고리즘
# 최고점, 최저점을 계속 갱신해서 차이가 가장 큰 것을 return
class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_value = sys.maxsize

        for price in prices:
            min_value = min(price, min_value)
            profit = max(price - min_value)
        
        return profit
