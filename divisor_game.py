"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:

    Input: 2
    Output: True

Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

    Input: 3
    Output: False
    
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """

        # I know that most people have already know this result, so I want to explain why Alice could always win when N is even.
        # The conclusion is that Alice could make moves such that Bob would always get an odd number and after Bob makes his move Alice would always get an even number.
        # For Alice, if she gets an even number, simply move from N to N - 1 so that N - 1 is odd now.
        # When Bob recieved an odd num N, all his moves would be M such that N % M == 0, which means that M is also odd.
        # This is because that if N % M == 0 and M is even then N would be even. Now Bob move from N to N - M and N - M is even since both of them are odd.
        # Now it is clear that Bob would keep getting odd numbers until it is 1 and lose the game.

        # If N = 1 (To win the game a player must bring another player to this stage.)
        # False

        # If N = 2
        # True

        # If N = 3
        # False

        # If N = 4
        # True

        # N = 5
        # False

        # N = 6
        # True

        # N = 7
        # False

        # N = 8
        # True

        # N = 9
        # False

        # Odd = Odd + Even
        # Even = Odd + Odd
        # Even =  Even + Even

        # Consider Alice having an odd number. From above it is clear that she will deduct an odd number from N and a new value of N will be even.

        # In case a player has an even number they just need to select x = 1 every time.
        # N % 1 = 0 and N-1 = Odd.
        # Once another player goes to an odd number it’s not possible to get out of this and will eventually reach 1.

        return N % 2 == 0

a = Solution()
print(a.divisorGame(6))
