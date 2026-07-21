# Leetcode problem : 217 Contains Duplicate

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for current in nums:
            if current in seen:
                return True
            seen.add(current)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example:
# Input: nums = [1,2,3,1]
# Output: True