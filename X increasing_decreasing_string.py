"""
Given a string s. You should re-order the string using the following algorithm:

1. Pick the smallest character from s and append it to the result.
2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the largest character from s and append it to the result.
5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:

    Input: s = "aaaabbbbcccc"
    Output: "abccbaabccba"
    Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
    After steps 4, 5 and 6 of the first iteration, result = "abccba"
    First iteration is done. Now s = "aabbcc" and we go back to step 1
    After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
    After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

    Input: s = "rat"
    Output: "art"
    Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

    Input: s = "leetcode"
    Output: "cdelotee"

Example 4:

    Input: s = "ggggggg"
    Output: "ggggggg"

Example 5:

    Input: s = "spo"
    Output: "ops"
"""


### OUTPUT LIMIT EXCEEDED ERROR ??? ###
### My original 'solution' edited with the correct 'solution'. Originally failed with 'leetcode' ###
class Solution(object):
    def sortString(self, s):
        # :type s: str
        # :rtype: str

        dict = {i:s.count(i) for i in s}
        seq = sorted(dict.keys())
        result = ""

        while sum(dict.values()) > 0:

            #temp = ''   # keeps track that only one character is appended
            for key in seq:
                #current, smallest = seq[i], seq[0]
                #if current >= smallest and temp != seq[i]:   # if current character is smaller and is different than previous character
                if dict[key] > 0:
                    result += key
                    print(result)
                    #temp = current
                    dict[key] -= 1 # subtracts 1 from the value of the current character
                    #if dict[current] == 0:   # removes key-value pair if value is 0
                        #del dict[current]

            #temp = ''
            for key in seq[::-1]:
                #current, largest = seq[i], seq[0]
                #if current <= largest and temp != seq[i]:
                if dict[key] > 0:
                    result += key
                    print(result)
                    #temp = current
                    dict[key] -= 1
                    #if dict[current] == 0:
                        #del dict[current]

            #seq = ''.join([k*v for k,v in dict.items()])   # converts key*value pair from remaining dictionary into the new string

        # print(dict)   # should be empty
        return result

a = Solution()
print(a.sortString("leetcode"))


"""
### Optimal Solution ###
class Solution:
    def sortString(self, s: str) -> str:
        raw = {i:s.count(i) for i in set(s)}
        seq = sorted(raw.keys())
        out = ""
        while sum(raw.values())>0:
            for i in seq:
                if raw[i]>0:
                    out+=i
                    raw[i]-=1
            for i in seq[::-1]:
                if raw[i]>0:
                    out+=i
                    raw[i]-=1
        return out


a = Solution()
print(a.sortString("leetcode"))
"""
