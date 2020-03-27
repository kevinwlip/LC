"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""

class Solution(object):
    def replaceElements(self, arr):
        # :type arr: List[int]
        # :rtype: List[int]

        largest = 0
        for i in range(len(arr)):
            try:
                largest = max(arr[i+1::])
            except:
                pass
            arr[i] = largest

        arr[-1] = -1
        return arr

a = Solution()
print(a.replaceElements([17,18,5,4,6,1]))


""" ### My Initial Solution
class Solution(object):
    def replaceElements(self, arr):
        # :type arr: List[int]
        # :rtype: List[int]

        largest = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] > largest:
                    largest = arr[j]
            arr[i] = largest
            largest = 0

        arr[-1] = -1
        return arr

a = Solution()
print(a.replaceElements([17,18,5,4,6,1]))
"""
