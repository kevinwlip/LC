"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:

    Input: A = [1], K = 0
    Output: 0

Explanation: B = [1]

Example 2:

    Input: A = [0,10], K = 2
    Output: 6

Explanation: B = [2,8]

Example 3:

    Input: A = [1,3,6], K = 3
    Output: 0

Explanation: B = [3,3,3] or B = [4,4,4]
"""

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        largest = max(A) - K
        smallest = min(A) + K
        difference = largest - smallest
        return 0 if difference < 0 else difference

'''
        diff = (max(A) - K) - (min(A) + K)   # Smallest Difference = decreased maximum - increased minimum

        all_ranges = []
        k_list = [i for i in range(-K, K+1)]   # List of all k-values
        for i in A:
            ok = list(map(lambda x: x+i, k_list))   # Add value in A to the the list of k values
            all_ranges.append(ok)

        no_diff = set.intersection(*map(set,all_ranges))   # No difference, duplicate values in all ranges can be constructed
        return 0 if no_diff else diff   # Return 0 if no difference else return smallest difference
'''

a = Solution()
print(a.smallestRangeI(A = [1,3,6], K = 3))
