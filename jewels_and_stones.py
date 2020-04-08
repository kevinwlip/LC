"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
    Output: 3
    Example 2:

Input: J = "z", S = "ZZ"
    Output: 0
    Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        #if len(J) > 50 or len(S) > 50 or len(list(set(J))) != len(J):
        #    return 0

        result = 0
        for i in J:
            for k in S:
                if i == k:
                    result += 1

        return result

a = Solution()
print(a.numJewelsInStones(J = "aA", S = "aAAbbbb"))
