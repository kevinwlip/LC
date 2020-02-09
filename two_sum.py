"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, next = 0, 0
        for pos in nums[start:]:
            for num in nums[start:]:
                try:
                    if next >= 0 and next < len(nums):
                        ret = nums[start] + nums[next]
                if ret == target:
                    return [start, next]
                next += 1
            start += 1
            next = start + 1

a = Solution()
print(a.twoSum([2, 7, 11, 15], 26))


"""
### Just the function ###
def twoSum(nums, target):
    start, next = 0, 0
    for pos in nums[start:]:
        for num in nums[start:]:
            try:
                if next >= 0 and next < len(nums):
                    ret = nums[start] + nums[next]
                #print("ret = ", ret)
            if ret == target:
                #print("Target reached: ", target)
                return [start, next]
            next += 1
        start += 1
        #print("start: ", start)
        next = start + 1
        #print("count: ", count)

print(twoSum([2, 7, 11, 15], 26))
"""

"""
### Good Solution ###
class Solution(object):
    def twoSum(self, nums, target):
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]

        h = {}
        for i, num in enumerate(nums):
            print("i:", i, " num:", num)
            n = target - num
            print("n:", n, " target:", target, " num:", num)
            if n not in h:
                h[num] = i
                print("h:", h)
            else:
                return [h[n], i]

a = Solution()
print(a.twoSum([2, 7, 11, 15], 22))
"""
