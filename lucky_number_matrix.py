"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    
Explanation:
    15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]

Explanation:
    12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
    Input: matrix = [[7,8],[1,2]]
    Output: [7]
"""

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        length, all_ele, min_val, min_index, lucky = len(matrix[0]), [y for x in matrix for y in x], 0, 0, []
        print(all_ele)
        for row_count, row in enumerate(matrix):
            min_val = row[0]
            for col_count, col in enumerate(row):
                if col < min_val:
                    min_val = col
                    min_index = col_count
            if min_val == max(all_ele[min_index::length]):
                lucky.append(min_val)

        return lucky

a = Solution()
print(a.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
