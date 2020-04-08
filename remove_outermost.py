"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
    Input: "(()())(())"
    Output: "()()()"

Explanation:
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
    Input: "(()())(())(()(()))"
    Output: "()()()()(())"

Explanation:
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
    Input: "()()"
    Output: ""

Explanation:
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".
"""

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """

        decomposition = []
        count, start = 0, 0
        for i, ele in enumerate(S):
            if ele == '(':
                count += 1
            elif ele == ')':
                count -= 1

            if count == 0:
                decomposition.append(S[start:i+1])
                start = i+1

        for j, ele2 in enumerate(decomposition):
            decomposition[j] = ele2[1:len(ele2)-1]

        return ''.join(decomposition)


a = Solution()
print(a.removeOuterParentheses("(()())(())(()(()))"))
