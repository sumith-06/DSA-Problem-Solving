# Leetcode problem: 1979. Find Greatest Common Divisor of Array

from typing import List

import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return math.gcd(nums[0], nums[len(nums)-1])

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Example:
# Input: nums = [2,5,6,9,10]
# Output: 2