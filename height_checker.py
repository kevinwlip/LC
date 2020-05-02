"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

Example 1:

    Input: heights = [1,1,4,2,1,3]
    Output: 3

Explanation:

    Current array : [1,1,4,2,1,3]
    Target array  : [1,1,1,2,3,4]

On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

Example 2:

    Input: heights = [5,1,2,3,4]
    Output: 5

Example 3:

    Input: heights = [1,2,3,4,5]
    Output: 0
"""

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        result = []

        for i in range(len(heights)):
            if heights[i] != sorted(heights)[i]:
                result.append(heights[i])

        return len(result)

a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))


### Another Solution ###
"""
class Solution(object):
    def heightChecker(self, heights):
        #:type heights: List[int]
        #:rtype: int

        result = 0

        for a,b in zip(heights, sorted(heights)):
            if a != b:
                result += 1

        return result



a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))
"""

### Another Solution II ###
"""
class Solution(object):
    def heightChecker(self, heights):
        #:type heights: List[int]
        #:rtype: int

        return sum([a != b for a, b in zip(heights, sorted(heights))])

a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))
"""

### Another Solution III ###
"""
class Solution(object):
    def heightChecker(self, heights):
        #:type heights: List[int]
        #:rtype: int

        output = list(map(lambda x: 1 if x[0] != x[1] else 0, zip(heights, sorted(heights))))
        return output.count(1)

a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))
"""
