"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        result, bin_count = [], 0
        bin_exp = sum(c.isalpha() for c in S)
        bin_list = [(bin(i).lstrip('0b')).zfill(len(bin((2**bin_exp)-1).lstrip('0b'))) for i in range(1, (2**bin_exp)+1)]
        bin_list[-1] = ''.zfill(len(bin_list[0]))
        #print(bin_list)

        for bin_num in bin_list:
            for i, char in enumerate(S):
                if char.isalpha() and bin_num[bin_count] == '0':
                    S = S[:i] + char.lower() + S[i+1:]
                    bin_count += 1
                elif char.isalpha() and bin_num[bin_count] == '1':
                    S = S[:i] + char.upper() + S[i+1:]
                    bin_count += 1
            bin_count = 0
            result.append(S)

        return result

a = Solution()
print(a.letterCasePermutation(S = "c9UJy"))


''' ### Dynamic Programming Solution ###
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        running_result =[""]
        for idx in range(len(S)):
            new_result = []
            if S[idx].isdigit():
                for word in running_result:
                    new_result.append(word + S[idx])
            else:
                for word in running_result:
                    new_result.append(word + S[idx].upper())
                    new_result.append(word + S[idx].lower())
            running_result = new_result
        return running_result
'''
