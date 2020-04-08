"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci].
For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Example 1:
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6

Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:
Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
"""

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """

        # create the matrix using a list comprehension
        matrix = [[0 for i in range(m)] for j in range(n)]

		# save the row and col values
        for i in indices:
            row = i[0]
            col = i[1]

            # increment the col
            for j in range(0, len(matrix)):
               matrix[j][col] += 1

            # increment the entire row specified
            matrix[row]= [s + 1 for s in matrix[row]]

        # find the number of cells with odd values by iterating through the matrix
        result = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    result += 1
        return result

a = Solution()
print(a.oddCells(2,3,[[0,1],[1,1]]))

"""
### O(n+m) using two arrays instead of O(nm) solution using a matrix ###
class Solution(object):
    def oddCells(self, n, m, indices):
        # :type n: int
        # :type m: int
        # :type indices: List[List[int]]
        # :rtype: int

        rows, cols = [0] * n, [0] * m
		for i, j in indices:
		    rows[i] += 1
			cols[j] += 1

        total  = 0
		for row in rows:
		    for col in cols:
			    total += (row + col) % 2
		return total

a = Solution()
print(a.oddCells(2,3,[[0,1],[1,1]]))
"""

"""
### Optimal Solution ###
class Solution(object):
    def oddCells(self, n, m, indices):
        # :type n: int
        # :type m: int
        # :type indices: List[List[int]]
        # :rtype: int

        rows, cols = [0] * n, [0] * m

        for i, j in indices:
            rows[i] += 1
            cols[j] += 1

        return sum((r + c) % 2 for r in rows for c in cols)

a = Solution()
print(a.oddCells(2,3,[[0,1],[1,1]]))
"""
