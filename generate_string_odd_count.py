"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.

Example 1:
    Input: n = 4
    Output: "pppz"

Explanation:
    "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:
    Input: n = 2
    Output: "xy"

Explanation:
    "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:
    Input: n = 7
    Output: "holasss"
"""

import random, string

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """

        return 'a' * n if n % 2 == 1 else ('a' * (n-1) + 'b')

'''
### Not a valid solution
        letters, i, result = {}, 0, ""
        while i != n:
            letter = random.choice(string.ascii_letters).lower()
            if letter in letters.keys():
                letters[letter] += 1
            else:
                temp = {letter:1}
                letters.update(temp)
            i += 1

        if any(n % 2 == 0 for n in letters.values()):
            self.generateTheString(n)

        for k, v in letters.items():
            result += k * v

        return result
'''

a = Solution()
print(a.generateTheString(10))
