"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

    Input: num = 5
    Output: 2

Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

    Input: num = 1
    Output: 0

Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        result = ''
        bin_num = bin(num).lstrip('0b')
        for i in range(len(bin_num)):
            if bin_num[i] == '0':
                result += '1'
            else:
                result += '0'

        return int(result, 2)

        #return num^(2**(len(bin(num)[2:]))-1)   # Alternative solution using XOR and bit manipulation,
                                                 # Obtains length of binary digits and subtracts 1, in binary form is all 1s
                                                 # Then 'num ^ digit  (XOR ^ converts to binary form)

a = Solution()
print(a.findComplement(4))
