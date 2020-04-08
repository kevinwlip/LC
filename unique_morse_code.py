"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:

Input: words = ["gin", "zen", "gig", "msg"]
Output: 2

Explanation:
    The transformation of each word is:
        "gin" -> "--...-."
        "zen" -> "--...-."
        "gig" -> "--...--."
        "msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""
### Elegant Solution
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        # :type words: List[str]
        # :rtype: int
        """

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lowercase = [chr(letter) for letter in range(97, 123)]
        encoding = dict(zip(lowercase, morse))
        code, result = "", []

        for word in words:
            result.append("".join(encoding[letter] for letter in word))

        return len(set(result))

a = Solution()
print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


"""
### My Original Solution ###
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        # :type words: List[str]
        # :rtype: int


        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lowercase = [chr(letter) for letter in range(97, 123)]
        encoding = dict(zip(lowercase, morse))
        code, result = "", []

        for i, word in enumerate(words):
            for j, letter in enumerate(word):
                if letter in encoding.keys():
                    code += encoding[letter]
                if len(word) == j+1:
                    result.append(code)
                    code = ""

        return len(set(result))

a = Solution()
print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
"""