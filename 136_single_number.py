# Leetcode problem : 136. Single Number

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: nums = [2,2,1]
# Output: 1