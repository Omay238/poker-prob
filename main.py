import itertools

cards: list[tuple[str, str]] = []
suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
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
					  ranks.index(hand[4][0]) - s
				  ] in [
		[1, 2, 3, 4],
		[1, 2, 3, 12]
	]:
		is_straight = True

	if hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]:
		is_flush = True
		if is_straight:
			is_straight_flush = True
			if s == 8:
				is_royal_flush = True

	if (hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] and hand[0][0] == hand[3][0] or
			hand[1][0] == hand[2][0] and hand[1][0] == hand[3][0] and hand[1][0] == hand[4][0]):
		is_four_of_a_kind = True

	if (hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] and hand[3][0] == hand[4][0] or
			hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[2][0] == hand[4][0]):
		is_full_house = True

	if (hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] or
			hand[1][0] == hand[2][0] and hand[1][0] == hand[3][0] or
			hand[2][0] == hand[3][0] and hand[2][0] == hand[4][0]):
		is_three_of_a_kind = True

	if (hand[0][0] == hand[1][0] and (hand[2][0] == hand[3][0] or hand[3][0] == hand[4][0]) or
	hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]):
		is_two_pair = True

	if (hand[0][0] == hand[1][0] or
			hand[1][0] == hand[2][0] or
			hand[2][0] == hand[3][0] or
			hand[3][0] == hand[4][0]):
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

print(f"royal flush:     {royal_flush}\n"
	  f"straight flush:  {straight_flush}\n"
	  f"four of a kind:  {four_of_a_kind}\n"
	  f"full house:      {full_house}\n"
	  f"flush:           {flush}\n"
	  f"straight:        {straight}\n"
	  f"three of a kind: {three_of_a_kind}\n"
	  f"two pair:        {two_pair}\n"
	  f"one pair:        {one_pair}\n"
	  f"high card:       {high_card}")
