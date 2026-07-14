#Given a binary array nums, return the maximum number of consecutive 1's in the array.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maximum = 0
        for num in nums:
            if num == 1:
                count += 1
                if maximum < count:
                    maximum = count
            else:
                count = 0
        return maximum

"""
Example:

Input: nums = [1,1,0,1,1,1]
Output: 3
"""