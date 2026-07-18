# Leetcode problem 977. Squares of a Sorted Array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
    
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Example:
# Input: nums = [-4,-1,0,3,10] 
# Output: [0,1,9,16,100]