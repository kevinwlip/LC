"""

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))

        return result

        # return ['FizzBuzz' if (num%3 ==0 and num%5 == 0) else 'Fizz' if num%3 ==0 else 'Buzz' if num%5 == 0 else str(num) for num in range(1, n+1)]   # One-liner

a = Solution()
print(a.fizzBuzz(15))
