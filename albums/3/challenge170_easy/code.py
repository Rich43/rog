'''
 (Easy): Blackjack Checker

Blackjack is a very common card game, where the primary aim is to pick up
cards until your hand has a higher value than everyone else but is less
than or equal to 21. This challenge will look at the outcome of the game,
rather than playing the game itself.

The value of a hand is determined by the cards in it.

    Numbered cards are worth their number - eg. a 6 of Hearts is worth 6.

    Face cards (JQK) are worth 10.

    Ace can be worth 1 or 11.

The person with the highest valued hand wins, with one exception - if a person has
5 cards in their hand and it has any value 21 or less, then they win automatically.
This is called a 5 card trick.

If the value of your hand is worth over 21, you are 'bust', and automatically lose.

Your challenge is, given a set of players and their hands, print who wins (or if it
is a tie game.)
Input Description

First you will be given a number, N. This is the number of players in the game.

Next, you will be given a further N lines of input. Each line contains the name
of the player and the cards in their hand, like so:

Bill: Ace of Diamonds, Four of Hearts, Six of Clubs

Would have a value of 21 (or 11 if you wanted, as the Ace could be 1 or 11.)
Output Description

Print the winning player. If two or more players won, print "Tie".
Example Inputs and Outputs
Example Input 1

3
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs

Example Output 1

Alice has won!

Example Input 2

4
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs
David: Two of Hearts, Three of Clubs, Three of Hearts, Five of Hearts, Six of Hearts

Example Output 2

David has won with a 5-card trick!
'''
import re

players = []
card_values = []

scores = 0

card_nums = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
             'Nine': 9, 'Ten':  10, 'Jack': 10, 'Queen': 10, 'King': 10}

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

hands1 = '''Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs'''

hands2 = '''Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs
David: Two of Hearts, Three of Clubs, Three of Hearts, Five of Hearts, Six of Hearts'''

hands = hands1.splitlines()

for line in hands:
    player = re.findall('^\w+', line)
    players.append(player[0])
print(players)

for line in hands:
    values = re.findall('\w+(?=\sof\s[Hearts|Clubs|Diamonds|Spades])', line)
    card_values.append(values)
print(card_values)

score_collection = []
for cards in card_values:
    for card in cards:
        scores += card_nums[card]
    score_collection.append(scores)
    scores = 0

print(score_collection)


accum = 0

for num in score_collection:
    if num > 21:
        continue