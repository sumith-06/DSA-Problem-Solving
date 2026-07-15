# """You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:
# sumOdd: the sum of the smallest n positive odd numbers.
# sumEven: the sum of the smallest n positive even numbers.
# Return the GCD of sumOdd and sumEven."""

#gcd of consecutive nums is 1 i.e gcd(n, n+1) = 1
#sumOdd = n**2, sumEven = n*(n+1)
# gcd(n**2, n(n+1)) -> n*gcd(n, n+1) -> n*1 = n

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
#Time complexity = O(1), Space complexity = O(1)

#first approach

# class Solution:
#     def gcdOfOddEvenSums(self, n: int) -> int:
#         sumOdd = n**2 #sum of first n positve odd numbers
#         sumEven = n*(n+1) #sum of first n positve even numbers
        
#         #Euclidean Algorithm
#         while sumOdd != 0:
#             R = sumEven % sumOdd
#             if R == 0:
#                 return sumOdd
#             else:
#                 sumEven = sumOdd
#                 sumOdd = R
