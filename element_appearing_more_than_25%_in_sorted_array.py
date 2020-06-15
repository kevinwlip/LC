"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

Example 1:

    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6
"""

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        return [i for i in arr if (arr.count(i) / len(arr)) > 0.25][0]

a = Solution()
print(a.findSpecialInteger(arr = [1,2,3,3]))
