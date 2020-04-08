"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dict = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if dict[prev] != i:
                    return False
        return not stack == 0

a = Solution()
print(a.isValid('('))
