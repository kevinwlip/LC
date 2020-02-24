"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        # :type x: int
        # :rtype: int

        if x <= -2**32 or x >= (2**32)-1:
            return 0
        string = str(x)
        if x >= 0:
            reversed = string[::-1]
        else:
            temp1 = string[1:]
            print(temp1)
            temp2 = temp1[::-1]
            print(temp2)
            reversed = "-" + temp2
            print(reversed)
        if int(reversed) <= -2**31 or int(reversed) >= (2**31)-1:
            return 0
        else:
            return int(reversed)

a = Solution()
print(a.reverse(0))


"""
### My solution using loops ###
class Solution(object):
    def reverse(self, x):
        # :type x: int
        # :rtype: int

        bitlist = []
        if x <= -2**32 or x >= (2**32)-1:
            return 0
        for i in str(x):
            bitlist.append(i)

        for count, j in enumerate(bitlist[::-1]):
            if j == "0":
                bitlist.pop()
            else:
                break
            #print("count:", count, "j:", j)

        bitlist = bitlist[::-1]

        if bitlist[len(bitlist)-1] == "-":
            bitlist.pop()
            bitlist.insert(0, "-")

        return int("".join(bitlist))

a = Solution()
print(a.reverse(-34))
"""
