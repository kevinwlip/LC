"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

    Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
    Output: ["girl","student"]

Example 2:

    Input: text = "we will we will rock you", first = "we", second = "will"
    Output: ["we","rock"]
"""

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

        result = []
        splitted = text.split()
        for i in range(len(splitted)-2):
            if first == splitted[i] and second == splitted[i+1]:
                result.append(splitted[i+2])

        return result

a = Solution()
print(a.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))
