"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

    Input: [3,1,2,4]
    Output: [2,4,3,1]

The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        result = []
        for num in A:
            if num % 2 == 0:
                result.insert(0, num)
            else:
                result.insert(len(result), num)

        return result

a = Solution()
print(a.sortArrayByParity([4,2,3,1]))
