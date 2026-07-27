# Leetcode Problem 442: Find All Duplicates in an Array

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input: nums = [4,3,2,7,8,2,3
# Output: [2,3]