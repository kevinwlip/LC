"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:

    Input: nums = [-3,2,-3,4,2]
    Output: 5

Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:

    Input: nums = [1,2]
    Output: 1

Explanation: Minimum start value should be positive.

Example 3:

    Input: nums = [1,-2,-3]
    Output: 5
"""

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos, step, temp = [i for i in range(1,sum(map(abs, nums)) + 1)], 0, []

        for i in pos:
            step = i + nums[0]
            temp.append(step)
            print(temp)
            for j in nums[1:]:
                step += j
                temp.append(step)
            if all(x >= 1 for x in temp):
                break
            else:
                temp = []

        return i

a = Solution()
print(a.minStartValue([-30,88,59,-11,-90,-95,-4,9,17,-43,98,-78,8,-75,-99,-78,-82,-42,43,72,82,-98,16,-12,-62,-27,-80,-49,-85,48,-59,12,-85,15,-48,-60,38,71,-56,53,-29,51,-40,33,-95,-50,-5,-41,-20,55,-29,-21,-2,-98,26,59,65,-40,24,-2,-47,90,-86,-90,-62,75,-80,-87,-15,5,-96,-27,-9,-55,37,-44,-49,-85,-77,28,-34,-80,-19,-98,-26,-72,64]))
