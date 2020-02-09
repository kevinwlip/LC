"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9.
* X can be placed before L (50) and C (100) to make 40 and 90.
* C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


### A solution which checks next symbol and add/subtracts accordingly ###
class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol, res = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}, 0

        for i in range(len(s) - 1):
            if symbol[s[i]] < symbol[s[i+1]]:
                res -= symbol[s[i]]
            else:
                res += symbol[s[i]]
        res += symbol[s[-1]]  # always add the last element
        return res

a = Solution()
print(a.romanToInt('MCMXCIV'))


"""
### A solution which checks the previous symbol adds/subtracts accordingly ###
class Solution(object):
    def romanToInt(self, s):

        # :type s: str
        # :rtype: int

        sym = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        total, prev = 0, 0
        for i in s:
            curr = sym[i]
            if curr is not None and curr > prev:
                total = total + curr - 2 * prev   # subtracts double the amount if prev value exists and smaller
            else:
                assert curr is not None
                total += curr
            prev = sym[i]

        return total


a = Solution()
print(a.romanToInt('MCMXCIV'))
"""

"""
### A solution which checks whether characters in the string matches 2 symbols or 1 symbol ###
class Solution(object):
    def romanToInt(self, s):

        # :type s: str
        # :rtype: int

        sym = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}

        total, index = 0, 0
        while index < len(s):
            curr = sym.get(s[index:index+2])
            if curr is not None:
                index += 2
            else:
                curr = sym.get(s[index])
                assert curr is not None
                index += 1
            total += curr

        return total


a = Solution()
print(a.romanToInt('MCMXCIV'))
"""
