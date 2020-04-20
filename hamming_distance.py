"""

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        result, bin_x, bin_y = 0, bin(x).replace('0b', ''), bin(y).replace('0b', '')
        print(bin_x, bin_y)

        while (len(bin_x) < len(bin_y)):
            bin_x = '0' + bin_x
        while (len(bin_x) > len(bin_y)):
            bin_y = '0' + bin_y

        print(bin_x, bin_y)
        for i in list(zip(bin_x, bin_y)):
            if i[0] != i[1]:
                result += 1

        return result

a = Solution()
print(a.hammingDistance(14, 2))
