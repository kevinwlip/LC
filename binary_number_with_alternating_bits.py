"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
    Input: 5
    Output: True

Explanation:
The binary representation of 5 is: 101

Example 2:
    Input: 7
    Output: False

Explanation:
The binary representation of 7 is: 111.

Example 3:
    Input: 11
    Output: False

Explanation:
The binary representation of 11 is: 1011.

Example 4:
    Input: 10
    Output: True

Explanation:
The binary representation of 10 is: 1010.
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        bin_n = bin(n).lstrip('0b')
        for i in range(len(bin_n) - 1):
            if bin_n[i] == '0' and bin_n[i+1] == '0' or bin_n[i] == '1' and bin_n[i+1] == '1':
                return False
        return True

a = Solution()
print(a.hasAlternatingBits(11))
