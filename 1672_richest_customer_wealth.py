# Leetcode Problem 1672: Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = wealth_of_i = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                wealth_of_i += accounts[i][j]
            if wealth_of_i > max_wealth:
                max_wealth = wealth_of_i
            wealth_of_i = 0
        return max_wealth
    
# Time Complexity: O(m*n) where n is the number of customers and m is the number of accounts per customer
# Space Complexity: O(1)

# Example:
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10