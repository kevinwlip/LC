"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:
    Input: s = "10#11#12"
    Output: "jkab"

Explanation:
    "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
    Input: s = "1326#"
    Output: "acz"

Example 3:
    Input: s = "25#"
    Output: "y"

Example 4:
    Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"
"""

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """

        keys = [str(i) if i < 10 else str(i)+"#" for i in range(1, 27)]
        values = [chr(i) for i in range(ord('a'), ord('z')+1)]
        mapping = dict(zip(keys, values))
        print(mapping)
        result, i = "", 0
        while i < len(s):
            try:
                if s[i+2] == '#':
                    mapping[s[i] + s[i+1] + s[i+2]]
                    result += mapping[s[i] + s[i+1] + s[i+2]]
                    i += 2

            except IndexError:
                pass

            if s[i] != '#':
                result += mapping[s[i]]
            i += 1

        return result

a = Solution()
print(a.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
