"""

"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        result, next_char, prev_char = [], S.find(C, 0), 0
        for i in range(len(S)):
            #print("char:", S[i], "next:", len(S[i:next_char]), "prev:", len(S[prev_char:i]))
            if len(S[i:next_char]) == 0 and S.find(C,i) != -1:
                result.append(len(S[i:next_char]))
                next_char = S.find(C, i+1)
                prev_char = S.find(C, i)
            elif len(S[prev_char:i]) <= len(S[i:next_char]) and i > S.find(C, 0):
                result.append(len(S[prev_char:i]))
            elif S.find(C, i) != - 1:
                result.append(len(S[i:next_char]))
            else:
                result.append(len(S[prev_char:i]))

        return result

a = Solution()
print(a.shortestToChar(S = "loveleetcode", C = 'e'))
