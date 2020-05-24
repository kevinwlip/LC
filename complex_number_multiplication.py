"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:

    Input: "1+1i", "1+1i"
    Output: "0+2i"

Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"

Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

1. The input strings will not have extra blank.
2. The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        x0 = int(a.split('+')[0])
        y0 = int(b.split('+')[0])
        x1 = int(a.split('+')[1].split('i')[0])
        y1 = int(b.split('+')[1].split('i')[0])

        first = x0 * y0
        second = str(x0 * y1 + x1 * y0) + 'i'
        third = (x1 * y1) * -1
        f_t = str(first + third)

        result = f_t + '+' + second

        return result

a = Solution()
print(a.complexNumberMultiply("1+-1i", "1+-1i"))
