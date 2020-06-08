"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
        for i, row in enumerate(A):
            for j, column in enumerate(row):
                if i == 0 and row == A[0]:
                    result.append([column])
                else:
                    result[j].append(column)

        return result

        # return [n for n in zip(*A)]   # One-liner solution

a = Solution()
print(a.transpose([[1,2,3],[4,5,6]]))
