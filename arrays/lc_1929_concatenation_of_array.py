# Problem: Concatenation of Array
# LeetCode: 1929
# Approach: Create a new array by appending the given array nums to itself. 
# This can be done by iterating through nums twice or by using list concatenation.
# Time Complexity:O(N)
# Space Complexity:O(N)

class Solution:
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[0]*(2*n)

        for i in range(n):
          ans[i]=nums[i]
          ans[i+n]=nums[i]

        return ans
