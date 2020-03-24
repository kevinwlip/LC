"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.

Example 1:

    Input: nums = [1,2,3,4]
    Output: [2,4,4,4]

    Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
    The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
    At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Constraints:

    2 <= nums.length <= 100
    nums.length % 2 == 0
    1 <= nums[i] <= 100
"""

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) < 2 or len(nums) > 100 or len(nums) % 2 != 0:
            print("Please enter an even lengthed list of integers between 1 and 100, inclusive")
            return 0

        curr, result = [], []
        for count, i in enumerate(nums):
            if nums[count] < 1 or nums[count] > 100:
                print("Please enter a valid index between 1 and 100, inclusive")
                return 0

            if count % 2 != 0:
                continue

            freq = nums[count]
            while freq != 0:
                curr.append(nums[count+1])
                freq -= 1

            result += curr
            curr = []

        return result

a = Solution()
print(a.decompressRLElist([1,2,3,4]))
