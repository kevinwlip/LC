"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8

Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Example 3:
    Input: grid = [[1,-1],[-1,-1]]
    Output: 3

Example 4:
    Input: grid = [[-1]]
    Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #m = len(grid)
        #if m < 1 or m > 100:
        #    return 0

        result = 0
        for count, i in enumerate(grid):
            #n = len(grid[count])
            #if n < 1 or n > 100:
            #    return 0
            for j in i:
                #if j < -100 or j > 100:
                #    return 0

                if "-" in str(j):
                    result += 1

        return result

a = Solution()
print(a.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

"""
### Binary Search, Optimal Solution O(mlogn)
class Solution(object):
    def countNegatives(self, grid):
        def bin(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid+1
            return len(row) - start

        count = 0
        for row in grid:
            count += bin(row)
        return(count)

a = Solution()
print(a.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
"""
