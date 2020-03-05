class Solution(object):
    def countAndSay(self, n):
        """
        # :type n: int
        # :rtype: str
        """
        if not n >= 1 or not n <= 30:
            return 0

        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        count_seq, match, next_seq_arr, result = 0, prev[0], [], ""

        for count, i in enumerate(prev):
            if match == prev[count]:
                count_seq += 1
            else:
                next_seq_arr.append(str(count_seq))
                next_seq_arr.append(match)
                count_seq = 1
                match = prev[count]

        next_seq_arr.append(str(count_seq))
        next_seq_arr.append(match)

        result = "".join(next_seq_arr)
        print("result", result)

        return result

a = Solution()
print(a.countAndSay(4))
