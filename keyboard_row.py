"""

"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        row_1 = 'qwertyuiop'
        row_2 = 'asdfghjkl'
        row_3 = 'zxcvbnm'

        def row_process(row, word):
            for char in word.lower():
                if char not in row:
                    break
            else:
                return word

        result, row_used = [], ''
        for word in words:
            if word[0].lower() in row_1:
                result.append(row_process(row_1, word))
            elif word[0].lower() in row_2:
                result.append(row_process(row_2, word))
            elif word[0].lower() in row_3:
                result.append(row_process(row_3, word))

        return [i for i in result if i]

a = Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))
