# Leetcode problem - 1464: Maximum Product of Two Numbers in an Array

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second_largest = 0
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
        return (largest - 1) * (second_largest - 1)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: nums = [3,4,5,2]
# Output: 12