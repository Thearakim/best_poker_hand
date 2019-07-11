# ROYAL_FLUSH = 9
# STRAIGHT_FLUSH = 8
# FOUR_OF_A_KIND = 7
# FULL_HOUSE = 6
# FLUSH = 5
# STRAIGHT = 4
# THREE_OF_A_KIND = 3
# TWO_PAIRS = 2
# ONE_PAIR = 1
# NO_PAIR = 0
#
# A = 14
# K = 13
# Q = 12
# J = 11
# T = 10

def checking_card1(p1):
    p1 = p1.split(" ")
    card1_number = list()
    card1_suit = list()
    for item in p1:                                                                     # assigning each card to seperate numbers and suit
        card1_number.append(item[0])
        card1_suit.append(item[1])


    if "A" or "K" or "Q" or "J" or "T" in card1_number:                             # converting all characters in the card to numbers
        card1_number = [1 if rank == "A" else rank for rank in card1_number]       #
        card1_number = [13 if rank == "K" else rank for rank in card1_number]       #
        card1_number = [12 if rank == "Q" else rank for rank in card1_number]       #
        card1_number = [11 if rank == "J" else rank for rank in card1_number]       #
        card1_number = [10 if rank == "T" else rank for rank in card1_number]       #
    min_rank = min(int(x) for x in card1_number)                                   # finding minimum number
    max_rank = max(int(x) for x in card1_number)                                   # findning maximum number


    chances_for_flush = None                                                        # checking for all FLUSH possibilities
    for card in card1_suit:
        check_suit = card1_suit.count(card)
        if check_suit == 5:
            chances_for_flush = True
    if chances_for_flush is True:
        if 1 in card1_number and 13 in card1_number and 12 in card1_number and 11 in card1_number and 10 in card1_number:
            # print("ROYAL FLUSH!!!!")                                        # returning as ROYAL_FLUSH
            return 9
        elif max_rank - min_rank == 4:
            # print("STRAIGHT FLUSH!!!")
            return 8                                                        # returnig STAIGHT_FLUSH
        else:
            # print("FLUSH!!!!")
            return 5                                                         # returning as FLUSH

    chances_for_no_pair = 0                                                  # checking for NO_PAIR
    checking_for_pairs = list()
    for card in card1_number:
        check_number = card1_number.count(card)
        if check_number == 2:
            checking_for_pairs.append(card)
        if check_number == 1:
            chances_for_no_pair += 1
    checking_for_pairs = set(checking_for_pairs)
    if chances_for_no_pair == 5:
        if max_rank - min_rank == 4:                                        # checking for STRAIGHT
            # print("STRAIGHT!!!")
            return 4                                                # returning as STRAIGHT
        # print("NO PAIR!!!!")
        return 0                                                    # returning as NO_PAIR
    elif chances_for_no_pair == 1 and len(checking_for_pairs) == 2:  # checking for TWO_PAIRS
        # print("TWO PAIRS!!!")
        return 2                                                        # returning as TWO_PAIRS
    elif chances_for_no_pair == 1:  # checking for FOUR_OF_A_KIND
        # print("FOUR OF A KIND!!!")
        return 7                                                        # returning as FOUR_OF_A_KIND
    elif chances_for_no_pair == 2:  # checking as THREE OF A KIND
        # print("THREE OF A KIND!!!")
        return 3                                                        # returning as THREE_OF_A_KIND
    elif chances_for_no_pair == 3:  # checking for ONE PAIR
        # print("ONE PAIR!!!")
        return 1                                                            # returning as ONE PAIR
    elif chances_for_no_pair == 0 and len(checking_for_pairs) == 1:  # checking for FULL HOUSE
        # print("FULL HOUSE!!!")
        return 6


def checking_card2(p2):
    p2 = p2.split(" ")
    card2_number = list()
    card2_suit = list()
    for item in p2:                                                                 # assigning each card to seperate numbers and suit
        card2_number.append(item[0])
        card2_suit.append(item[1])


    if "A" or "K" or "Q" or "J" or "T" in card2_number:                             # converting all characters in the card to numbers
        card2_number = [1 if rank == "A" else rank for rank in card2_number]       #
        card2_number = [13 if rank == "K" else rank for rank in card2_number]       #
        card2_number = [12 if rank == "Q" else rank for rank in card2_number]       #
        card2_number = [11 if rank == "J" else rank for rank in card2_number]       #
        card2_number = [10 if rank == "T" else rank for rank in card2_number]       #
    min_rank = min(int(x) for x in card2_number)                                   # finding minimum number
    max_rank = max(int(x) for x in card2_number)                                   # findnig maximum number


    chances_for_flush = None                                                            # checking for all FLUSH possibilities
    for card in card2_suit:
        check_suit = card2_suit.count(card)
        if check_suit == 5:
            chances_for_flush = True
    if chances_for_flush == True:
        if 1 in card2_number and 13 in card2_number and 12 in card2_number and 11 in card2_number and 10 in card2_number:
            # print("ROYAL FLUSH!!!!")                        # returning as ROYAL_FLUSH
            return 9
        elif max_rank - min_rank == 4:
            # print("STRAIGHT FLUSH!!!")
            return 8                                # returnig STAIGHT_FLUSH
        else:
            # print("FLUSH!!!!")
            return 5                                # returning as FLUSH


    chances_for_no_pair = 0                                 # checking for NO_PAIR
    checking_for_pairs = list()
    for card in card2_number:
        check_number = card2_number.count(card)
        if check_number == 2:
            checking_for_pairs.append(card)
        if check_number == 1:
            chances_for_no_pair += 1
    checking_for_pairs = set(checking_for_pairs)
    if chances_for_no_pair == 5:
        if max_rank - min_rank == 4:            # checking for STRAIGHT
            # print("STRAIGHT!!!")
            return 4                            # returning as STRAIGHT
        # print("NO PAIR!!!!")
        return 0                                # returning as NO_PAIR
    elif chances_for_no_pair == 1 and len(checking_for_pairs) == 2:              # checking for TWO_PAIRS
        # print("TWO PAIRS!!!")
        return 2                                # returning as TWO_PAIRS
    elif chances_for_no_pair == 1:              # checking for FOUR_OF_A_KIND
        # print("FOUR OF A KIND!!!")
        return 7                                # returning as FOUR_OF_A_KIND
    elif chances_for_no_pair == 2:              # checking as THREE OF A KIND
        # print("THREE OF A KIND!!!")
        return 3                                # returning as THREE_OF_A_KIND
    elif chances_for_no_pair == 3:              # checking for ONE PAIR
        # print("ONE PAIR!!!")
        return 1                                # returning as ONE PAIR
    elif chances_for_no_pair == 0 and len(checking_for_pairs) == 1:             # checking for FULL HOUSE
        # print("FULL HOUSE!!!")
        return 6


def poker_hand(p1, p2):                                                         # seperating player cards into suit and number
    p1_rank = checking_card1(p1)
    p2_rank = checking_card2(p2)
    if p1_rank == 9 or p1_rank > p2_rank:
        return "Player 1 WIN"
    elif p2_rank == 9 or p1_rank < p2_rank:
        return "Player 2 WIN"
    else:
        return "Tie"


# print(poker_hand("AH KS QH JH TH", "AS KH QC JC TC"))
# print(poker_hand("8D 4C 7H 5H 6S", "9S 4S 8C 6H 5S"))
# print(poker_hand("3H 4H 5H 6H 7H", "5D 6D 7D 8H 9D"))
# print(poker_hand("AH KS QH JH TH", "AS KH QC JC TC"))
# print(poker_hand("8D 8C 7H 7H 6S", "9S 9S 5C 5H 4S"))
# print(poker_hand("3H 4H 5H 6H 7H", "5D 6D 7D 8H 9D"))
# print(poker_hand("AH KH QH JH TH","7H 7S 7D 6H 9H"))
