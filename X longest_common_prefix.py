"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
    All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        # :type strs: List[str]
        # :rtype: str
        """

        count, char_count, vals, prefix = 0, 0, [], []

        def test(char_count):
            for count, word in enumerate(strs):
                vals.append(strs[count][char_count])
                if count == (len(strs)-1) and all(x == strs[count][char_count] for x in vals):   # The all() checks that all values are the same in the list
                    prefix.append(strs[count][char_count])
                    vals[:] = []
                    char_count += 1
                    test(char_count)

            return "".join(prefix)

        return test(char_count) if len(strs) != 1 else strs[0]
        #print("prefix: ", prefix)   # List of letters in the prefix
        #print("vals: ", vals)   # list of first unmatching letter in each word

a = Solution()
print(a.longestCommonPrefix(["leets","leetcode","leetc", "leeds"]))

"""
### Another Solution ###
class Solution:
    def longestCommonPrefix(self, strs):

        #:type strs: List[str]
        #:rtype: str

        if not strs: return ""
        if len(strs) == 1: return strs[0]

        strs.sort()
        prefix = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: prefix += x
            else: break
        return prefix

a = Solution()
print(a.longestCommonPrefix(["leets","leetcode","leetc", "leeds"]))
"""

"""
### Another Solution II ###
class Solution:
    def longestCommonPrefix(self, strs):

        # :type strs: List[str]
        # :rtype: str

        prefix=[]
        num = len(strs)
        for x in zip(*strs):   # '*strs' unpacks the iterable, 'zip()' is then applied on the elements
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)

a = Solution()
print(a.longestCommonPrefix(["leets","leetcode","leetc", "leeds"]))
"""

"""
### Another Solution III ###
class Solution:
    def longestCommonPrefix(self, strs):

        prefix = ""
        for i in xrange(len(min(strs))):   # xrange returns a generator object, i = 0,1,2,..., etc
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                prefix += c
            else:
                break
        print("length", len(strs))
        return prefix if len(strs) != 0 else ""

a = Solution()
print(a.longestCommonPrefix(["leets","leetcode","leetc", "leeds"]))
"""
