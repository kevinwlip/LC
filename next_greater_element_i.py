"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]

Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]

Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result, nums2_index = [], 0

        for i in range(len(nums1)):
            nums2_index = nums2.index(nums1[i])
            for j in range(nums2_index+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)

        return result

a = Solution()
print(a.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
