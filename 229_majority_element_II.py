# Leetcode Problem 229: Majority Element II

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        res = []
        n = len(nums)
        for key, value in freq.items():
            if value > n//3:
                res.append(key)
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# Example:
# Input: nums = [3,2,3]
# Output: [3]