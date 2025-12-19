# Poker Hands
## Description
Poker is a famous gambling game, where you have 5 cards, and bet based on how good they meet specific criterias. There are many variants, however I will not be covering any of those. You draw 5 random cards from a deck, and can score them.

## Events
The events I chose are just all of the possible poker hands (ignoring individual rankings, since according to Wikipedia there's 7,462 of those)

## Assumptions
 - Standard 52 card French deck without Jokers.
 - Draw 5 cards regularly with no other influences.
 - One draw.
 - Dependent events, as once a card is drawn, it can't be drawn again.
 - Standard Poker score rules.

## Probabilities
### Total Scenarios
There are 52 cards in a deck, you draw 5, and order does not matter. So, you can use the combination formula as below.

$\frac{52!}{(52-5)!5!}=\frac{52!}{47!5!}=\frac{52\cdot51\cdot50\cdot49\cdot48}{5\cdot4\cdot3\cdot2\cdot1}=\frac{311875200}{120}=2598960$

### Royal Flush
A Royal Flush is when you have the 5 highest cards of a single suit &mdash; Ace, King, Queen, Jack, and 10. Theres only one possibility of it per suit, with 4 suits, therefore only 4 Royal Flushes in the game. (By the way; this only differs to Straight Flush for style points. There's no real difference)

$1\cdot4=4\to\frac{4}{2598960}\approx0.00000154=0.000154\%$

These are **very** poor odds for a player, being one in around 680,000, which is reasonable for the best hand in the entire game.

### Straight Flush
A Straight Flush is when you have a Straight, or 5 cards in order, of a single suit. There's 10 possible Straights, being from Ace-Low to 10-Low (with 5-High and Ace-High respectively), for each suit. Note that one should be removed because that's a Royal Flush, and they are counted seperately.

$(10-1)\cdot4=9\cdot4=36\to\frac{36}{2598960}\approx0.00001385=0.001385\%$

The Straight Flush is more common than the Royal Flush, however it is still incredibly rare. It's unlikely to get, and really, should be counted alongside the Royal Flush, even which is very unreasonable to get.

### Four of a Kind
There are 13 ranks of cards, each with a potential Four of a Kind available. Then, after those 4 cards are uses, it leaves 48 possible cards that can make up the solo card.

$13\cdot48=624\to\frac{624}{2598960}\approx0.0002401=0.02401\%$

This, again, is quite rare, although I believe we are beginning to get into more reasonable territory. This would reasonably occur in around 2000 games of drawing 5, which is more likely in a popular variant like Texas Hold 'Em. 

### Full House
A Full House is when you have a pair _**and**_ a trio. For each rank, there are 4 possible triples $\frac{4!}{1!3!}$, and 6 pairs $\frac{4!}{2!2!}$. Theres 13 ranks, but one needs to be skipped for either the pair or the trio, because they can't both be the same.

$4\cdot13\cdot6\cdot12=3744\to\frac{3744}{2598960}\approx0.00144058=0.144058\%$

This is I believe the turning point. Probably occuring in around 300 games, many players have likely seen this at least once. Regardless, it's still uncommon. 

### Flush
A Flush is when all of your cards are in a single suit. You must pick your 5 cards from the subset which is a single suit. And, also, remove the Royal and Straight Flushes from this, because they are higher scoring and should not be counted.

$\frac{13!}{(13-5)!5!}=\frac{13!}{8!5!}=\frac{13\cdot12\cdot11\cdot10\cdot9}{5\cdot4\cdot3\cdot2\cdot1}=\frac{154440}{120}=1287\to1287\cdot4=5148\to5148-36-4=5108\to\frac{5108}{2598960}\approx0.0019654=0.19654\%$

This is the highest score I've personally gotten. Occuring by around 250 games, this is where I'd expect most players to have gotten it. It's a moderately reasonable assumption, if your personal cards are both the same suit, you could go for a Flush. 

### Straight
Again, there are 10 possible Straights, which I don't need to cover again. But, there are 5 possibilities for different suits, of which there are 4. And, as with flushes, we must remove the Royal and Straight Flushes.

$10\cdot4^5=10\cdot1024=10240\to10240-36-4=10200\to\frac{10200}{2598960}\approx0.00392465=0.392465\%$

It feels like I've been so close to a Straight so many times, but have never gotten it. It's clearly plausible because of the .4%, which is low, but not 0.

### Three of a Kind
Like the trio in the Full House, there are 4 possible trios per rank, across 13 ranks. The other two cards can any suit, and rank that isn't shared with the trio or other single card.

$13\cdot4\cdot\frac{12!}{(12-2)!2!}\cdot4^2=13\cdot4\cdot\frac{12!}{10!2!}\cdot16=13\cdot4\cdot\frac{12\cdot11}{2}\cdot16=13\cdot4\cdot\frac{132}{2}\cdot16=13\cdot4\cdot66\cdot16=54912\to\frac{54912}{2598960}\approx0.02112845=2.112845\%$

I haven't gotten this one, due to poor luck, however I've run a fair few games where the winner had Three of a Kind, so it's definitely quite common, compared to the previous entries. 

### Two Pair
Two Pair, is, of course, when you have two pairs. There's 2 neccessary different ranks, each with 2 different suits, along with one other card that must fall with a different rank.

$\frac{13!}{(13-2)!2!}\cdot6\cdot6\cdot11\cdot4=\frac{13!}{11!2!}\cdot6\cdot6\cdot11\cdot4=\frac{13\cdot12}{2}\cdot6\cdot6\cdot11\cdot4=\frac{156}{2}\cdot6\cdot6\cdot11\cdot4=78\cdot6\cdot6\cdot11\cdot4=123552\to\frac{123552}{2598960}\approx0.04753902=4.753902\%$

A Two Pair is even more common, with around a 5% probability. It feels quite often when playing that it appears. It's again a reasonable thing to go for. 

### One Pair
Shockingly, One Pair is when you have one pair. Once again, there's 13 possible ranks, any suit, and 3 other cards. You get the gist by now.

$13\cdot6\cdot\frac{12!}{(12-3)!3!}\cdot4\cdot4\cdot4=13\cdot6\cdot\frac{12!}{9!3!}\cdot4\cdot4\cdot4=13\cdot6\cdot\frac{12\cdot11\cdot10}{3\cdot2}\cdot4\cdot4\cdot4=13\cdot6\cdot\frac{1320}{6}\cdot4\cdot4\cdot4=13\cdot6\cdot220\cdot4\cdot4\cdot4=1098240\to\frac{1098240}{2598960}\approx0.42256903=42.256903\%$

This, is finally, incredibly common. Pretty much every game I run has at least one of these somewhere. Nearly half of the hands you can have a pair somewhere in them. 

### High Card
High Card is anything left, so, you can just sum up all the other possibilities, subtract it from the total, and boom &mdash; high cards.

$4+36+624+3744+5108+10200+54912+123552+1098240=1296420\to2598960-1296420=1302540\to\frac{1302540}{2598960}\approx0.50117739=50.117739\%$

This is most common, which makes sense because it's just the wild card category. The fact that it does make up over half is a bit surprising though — that's pretty significant. 

## Conclusions
The differences between the different card combinations are quite impressive, and while it seems accurate, having just over half of all possible hands being pretty much nothing is shocking to me.

Also, while I expected it, they are in order of most probable to least probable. I am a bit curious as to when these hand combinations were decided, and how. I assume they used the same/similar method to me, as it was certainly before computing.

The one that seems to most often make or break a round is a two pair, because it's common enough that typically someone can get it, although rare enough that it'll beat everyone else most of the time. 

## Validation
I wrote an admittedly inefficient program to calculate all of the card outcomes and it did output the same results for odds.

```
royal flush...........4
straight flush.......36
four of a kind......624
full house.........3744
flush..............5108
straight..........10200
three of a kind...54912
two pair.........123552
one pair........1098240
high card.......1302540
```
<details>
<summary>Code</summary>

```python
import itertools

cards: list[tuple[str, str]] = []
suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = [
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "jack",
    "queen",
    "king",
    "ace",
]
for suit in suits:
    for rank in ranks:
        cards.append((rank, suit))

royal_flush = 0
straight_flush = 0
four_of_a_kind = 0
full_house = 0
flush = 0
straight = 0
three_of_a_kind = 0
two_pair = 0
one_pair = 0
high_card = 0

for hand in itertools.combinations(cards, 5):
    hand = sorted(hand, key=lambda x: ranks.index(x[0]))

    is_royal_flush = False
    is_straight_flush = False
    is_four_of_a_kind = False
    is_full_house = False
    is_flush = False
    is_straight = False
    is_three_of_a_kind = False
    is_two_pair = False
    is_one_pair = False

    s = ranks.index(hand[0][0])
    if [
        ranks.index(hand[1][0]) - s,
        ranks.index(hand[2][0]) - s,
        ranks.index(hand[3][0]) - s,
        ranks.index(hand[4][0]) - s,
    ] in [[1, 2, 3, 4], [1, 2, 3, 12]]:
        is_straight = True

    if (
        hand[0][1] == hand[1][1]
        and hand[0][1] == hand[2][1]
        and hand[0][1] == hand[3][1]
        and hand[0][1] == hand[4][1]
    ):
        is_flush = True
        if is_straight:
            is_straight_flush = True
            if s == 8:
                is_royal_flush = True

    if (
        hand[0][0] == hand[1][0]
        and hand[0][0] == hand[2][0]
        and hand[0][0] == hand[3][0]
        or hand[1][0] == hand[2][0]
        and hand[1][0] == hand[3][0]
        and hand[1][0] == hand[4][0]
    ):
        is_four_of_a_kind = True

    if (
        hand[0][0] == hand[1][0]
        and hand[0][0] == hand[2][0]
        and hand[3][0] == hand[4][0]
        or hand[0][0] == hand[1][0]
        and hand[2][0] == hand[3][0]
        and hand[2][0] == hand[4][0]
    ):
        is_full_house = True

    if (
        hand[0][0] == hand[1][0]
        and hand[0][0] == hand[2][0]
        or hand[1][0] == hand[2][0]
        and hand[1][0] == hand[3][0]
        or hand[2][0] == hand[3][0]
        and hand[2][0] == hand[4][0]
    ):
        is_three_of_a_kind = True

    if (
        hand[0][0] == hand[1][0]
        and (hand[2][0] == hand[3][0] or hand[3][0] == hand[4][0])
        or hand[1][0] == hand[2][0]
        and hand[3][0] == hand[4][0]
    ):
        is_two_pair = True

    if (
        hand[0][0] == hand[1][0]
        or hand[1][0] == hand[2][0]
        or hand[2][0] == hand[3][0]
        or hand[3][0] == hand[4][0]
    ):
        is_one_pair = True

    if is_royal_flush:
        royal_flush = royal_flush + 1
    elif is_straight_flush:
        straight_flush = straight_flush + 1
    elif is_four_of_a_kind:
        four_of_a_kind = four_of_a_kind + 1
    elif is_full_house:
        full_house = full_house + 1
    elif is_flush:
        flush = flush + 1
    elif is_straight:
        straight = straight + 1
    elif is_three_of_a_kind:
        three_of_a_kind = three_of_a_kind + 1
    elif is_two_pair:
        two_pair = two_pair + 1
    elif is_one_pair:
        one_pair = one_pair + 1
    elif True:
        high_card = high_card + 1

print(
    f"royal flush:     {royal_flush}\n"
    f"straight flush:  {straight_flush}\n"
    f"four of a kind:  {four_of_a_kind}\n"
    f"full house:      {full_house}\n"
    f"flush:           {flush}\n"
    f"straight:        {straight}\n"
    f"three of a kind: {three_of_a_kind}\n"
    f"two pair:        {two_pair}\n"
    f"one pair:        {one_pair}\n"
    f"high card:       {high_card}"
)
```
</details>
