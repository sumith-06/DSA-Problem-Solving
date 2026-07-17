# Leetcode Problem: 268. Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8