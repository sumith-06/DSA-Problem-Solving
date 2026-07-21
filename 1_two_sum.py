# Leetcode problem : 1.Two sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in seen:
                return [i, seen[complement]]
            seen[current] = i

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]