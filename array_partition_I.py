"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
    Input: [1,4,3,2]
    Output: 4

Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ordered = sorted(nums)
        sum = 0

        for i in range(0, len(ordered), 2):
            sum += min([ordered[i], ordered[i+1]])

        return sum

a = Solution()
print(a.arrayPairSum([1,4,3,2]))


### One liner solution, Pattern: every other element gets added ###
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        # :type nums: List[int]
        # :rtype: int
        """

        return sum(sorted(nums)[::2])

a = Solution()
print(a.arrayPairSum([1,4,3,2]))
"""
