"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

    Input: arr = [1,2,2,1,1,3]
    Output: true

Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

    Input: arr = [1,2]
    Output: false

Example 3:

    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        dict = {i: arr.count(i) for i in set(arr)}
        return True if len(set(dict.values())) == len(dict.values()) else False

a = Solution()
print(a.uniqueOccurrences([1,2,2,1,1,3]))
