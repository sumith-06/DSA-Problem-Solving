# Leetcode problem : 121. Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, max_profit = prices[0], 0
        for current_price in prices:
            if current_price < buy_price:
                buy_price = current_price
            else:
                max_profit = max(max_profit, current_price - buy_price)
        return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5