# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq = 0
        for i in range(len(nums)):
            if nums[unq] != nums[i]:
                unq += 1
                nums[unq], nums[i] = nums[i], nums[unq]
        return unq+1
    
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: function  return unq = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.