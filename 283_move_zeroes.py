#Given an integer array nums, move all 0's to the end of it 
#while maintaining the relative order of the non-zero elements.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

"""
Example:

Input: nums = [0,1,0,3,12]
Output: nums updated as [1,3,12,0,0]
"""