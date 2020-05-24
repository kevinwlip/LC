"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Example 1:

    Input: s = "leetcode"
    Output: 2

Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

    Input: s = "abbcccddddeeeeedcba"
    Output: 5

Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:

    Input: s = "triplepillooooow"
    Output: 5

Example 4:

    Input: s = "hooraaaaaaaaaaay"
    Output: 11

Example 5:

    Input: s = "tourist"
    Output: 1
"""

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """

        result, start = [], 0

        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                result.append(s[start:i+1])
                start = i+1
        result.append(s[start:])   # Append the last character(s) to the list
        result = max((map(len, result)))

        return result

a = Solution()
print(a.maxPower("tourist"))
