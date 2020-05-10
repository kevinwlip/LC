"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

    Input: [4,2,5,7]
    Output: [4,5,2,7]

Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        result, even, odd = [], 0, 1
        for i, ele in enumerate(A):
            if ele % 2 == 0:
                result.insert(even, ele)
                even += 2
            else:
                result.insert(odd, ele)
                odd += 2

        return result

a = Solution()
print(a.sortArrayByParityII([2,4,5,1,6,3]))
