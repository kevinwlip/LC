class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        check = []

        for i in nums:
            if(check.count(i) == 2):
                check.remove(i)
                check.remove(i)
            else:
                check.append(i)

        return check[0]



        print(nums)
        print(slice)
'''
        for i in nums:
            if i not in no_duplicate_map:
                no_duplicate_map.append(i)
            else:
                no_duplicate_map.remove(i)
        return no_duplicate_map.pop()
'''
a = Solution()
print(a.singleNumber([3,3,5,3,2,2,2]))
