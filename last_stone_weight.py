"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

    Input: [2,7,4,1,8,1]
    Output: 1

Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        new_stones, diff = sorted(stones, reverse = True), 0

        for i, stones in enumerate(new_stones):
            if len(new_stones) == 1:
                return new_stones[0]

            elif len(new_stones) >= 2:
                diff = new_stones[i] - new_stones[i+1]
                new_stones.append(diff)
                del new_stones[1]
                del new_stones[0]
                return self.lastStoneWeight(new_stones)

a = Solution()
print(a.lastStoneWeight([2,7,4,1,8,100]))
