# Leetcode problem - 4. Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        n = len(merged_array)
        if n % 2 == 1:
            return float(merged_array[((n+1)//2)-1])
        else:
            return (merged_array[n//2-1]+ merged_array[n//2])/2
        
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)
# m and n are the lengths of nums1 and nums2 respectively.

# Example:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000