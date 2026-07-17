#Leetcode problem - 3869.Sum of GCD of formed pairs

from typing import List
import math 

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        pgcd = [0]*n
        maximum = 0
        for i in range (n):
            maximum = max(maximum, nums[i])
            pgcd[i] = math.gcd(nums[i], maximum)
        pgcd.sort()
        l = 0
        r = n-1
        total = 0
        while l < r:
            total += math.gcd(pgcd[l],pgcd[r])
            l += 1
            r -= 1
        return total 

# Time Complexity = O(n log n)
# Space Complexity = O(n)

# Example:
# Input: nums = [3,6,2,8]
# Output: 5
