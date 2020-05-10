"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:

    Input: "IDID"
    Output: [0,4,1,3,2]

Example 2:

    Input: "III"
    Output: [0,1,2,3]

Example 3:

    Input: "DDI"
    Output: [3,2,0,1]
"""

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        result.append(0) if S[0] == 'I' else result.append(len(S))
        if result[0] == 0:
            n = [i+1 for i in range(len(S))]
        else:
            n = [i for i in range(len(S))]

        for i in range(len(S)):
            try:
                if S[i] == 'I' and S[i+1] == 'I':
                    result.append(min(n))
                    n.remove(min(n))
                elif S[i] == 'I' and S[i+1] == 'D':
                    result.append(max(n))
                    n.remove(max(n))
                elif S[i] == 'D' and S[i+1] == 'I':
                    result.append(min(n))
                    n.remove(min(n))
                elif S[i] == 'D' and S[i+1] == 'D':
                    result.append(max(n))
                    n.remove(max(n))
            except:
                pass

        result.extend(n)
        return result

a = Solution()
print(a.diStringMatch("III"))


""" ### Two-Pointer Solution ###
class Solution(object):
    def diStringMatch(self, S):
        #:type S: str
        #:rtype: List[int]

        i, d = 0, len(S)
        res = []
        for _ in range(len(S)):
            if S[_] == "I":
                res.append(i)
                i += 1
            else:
                res.append(d)
                d -= 1
        res.append(i)
        return res

"""
