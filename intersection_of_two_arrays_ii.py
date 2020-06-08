"""
Given two arrays, write a function to compute their intersection.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        uniques = list(set(nums1) & set(nums2))
        one = {i:nums1.count(i) for i in uniques}
        two = {i:nums2.count(i) for i in uniques}

        for i in uniques:
            if one[i] <= two[i]:
                result.extend([i] * one[i])
            else:
                result.extend([i] * two[i])

        return result

a = Solution()
print(a.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
