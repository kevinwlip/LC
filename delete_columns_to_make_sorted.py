"""

"""

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        columns, result = list(zip(*A)), []

        for i in range(len(columns)):
            if list(columns[i]) != sorted(list(columns[i])):
                result.append(i)

        return len(result)

a = Solution()
print(a.minDeletionSize(["zyx","wvu","tsr"]))
