#Given a zero-based permutation nums (0-indexed), build an array ans of the same length
#where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
    
"""
Example:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
"""