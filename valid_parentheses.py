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
        for count, i in enumerate(s):
            if i in dict.keys():
                stack.append(i)
            elif dict.get(stack[-1]) == i:
                #print("i", i, "dict", dict.get(stack[-1]))
                stack.pop()
            else:
                stack.append(i)
            #print('count', count, 'stack', stack)

        return True if len(stack) == 0 else False

a = Solution()
print(a.isValid('((()(())))'))
