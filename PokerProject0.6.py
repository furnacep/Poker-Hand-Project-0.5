Deck_cards = ["as", "ah", "ac", "ad", "ks", "kh", "kc", "kd", "qs", "qh", "qc", "qd", "js", "jh", "jc", "jd", "10s",
              "10h", "10c", "10d", "9s", "9h", "9c", "9d", "8s", "8h", "8c", "8d", "7s", "7h", "7c", "7d", "6s", "6h",
              "6c", "6d", "5s", "5h", "5c", "5d", "4s", "4h", "4c", "4d", "3s", "3h", "3c", "3d", "2s", "2h", "2c",
              "2d"]

# asking user for the hole cards
Hole_card1 = str(raw_input("Please select a hole card (e.g. Ah):")).lower()
if Hole_card1 not in Deck_cards:
    Hole_card1 = raw_input("Whoops, lets try again, please select a hole card with a suit:")

Hole_card2 = str(raw_input("please select a second hole card(e.g. Kh):")).lower()
if Hole_card2 in Deck_cards:
    pass
elif Hole_card2 == Hole_card1:
    Hole_card2 = raw_input("Whoops, lets try again, please select a second hole card with a suit:")
else:
    Hole_card2 = raw_input("Whoops, lets try again, please select a second hole card with a suit:")


# identifying the suit card
def hole_card_suit(holecard):
    return holecard[-1]

Hole_card_suits = hole_card_suit(Hole_card1) + hole_card_suit(Hole_card2)

# asking user for the board cards
board_card1 = str(raw_input("Please provide 1st card for the board:"))
board_card2 = str(raw_input("Please provide 2nd card for the board:"))
board_card3 = str(raw_input("Please provide 3rd card for the board:"))
board_card4 = str(raw_input("Please provide 4th card for the board:"))
board_card5 = str(raw_input("Please provide 5th card for the board:"))

Full_board = [board_card1, board_card2, board_card3, board_card4, board_card5, Hole_card1, Hole_card2]


# identifying the board card suit
def board_suit(board_card):
    return board_card[-1]


# identifying the cards without suits!
def cards_no_suits(cards):
    if cards.__contains__("10"):
        return cards[0:2]
    else:
        return cards[0]

Full_board_no_suits = [cards_no_suits(Hole_card1), cards_no_suits(Hole_card2), cards_no_suits(board_card1),
                       cards_no_suits(board_card2), cards_no_suits(board_card3), cards_no_suits(board_card4),
                       cards_no_suits(board_card5)]

# def pair
blank = []
pairs_present = []
for c in Full_board_no_suits:
    if blank.__contains__(c):
        pairs_present.append(c)
    else:
        blank.append(c)
pair = 0
if len(pairs_present) == 1:
    pair = 1


# def trips
blank2 = []
trips_present = []
for c in pairs_present:
    if blank2.__contains__(c):
        trips_present.append(c)
    else:
        blank2.append(c)
trips = 0
if len(trips_present) == 1:
    trips = 1

# def quads
blank3 = []
quads_present = []
for c in trips_present:
    if blank3.__contains__(c):
        quads_present.append(c)
    else:
        blank3.append(c)
if len(quads_present) >= 1:
    quads = 1
else:
    quads = 0

# def two pair
two_pair = False
if len(pairs_present) >= 2 and trips_present == 0:
    two_pair = True

# def full house
full_house = 0
if (len(pairs_present) >= 2) and (trips == 1) and (quads == 0):
    full_house = 1

# def straight
Change_AKQJ = []
for c in Full_board_no_suits:
    if (c == "2") or (c == "3") or (c == "4") or (c == "5") or (c == "6") or (c == "7") or (c == "8") or (c == "9") or \
       (c == "10"):
        Change_AKQJ.append(c)
    elif c == "a":
        Change_AKQJ.append(1)
    elif c == "k":
        Change_AKQJ.append(13)
    elif c == "q":
        Change_AKQJ.append(12)
    else:
        Change_AKQJ.append(11)

ordered = []
for c in Change_AKQJ:
    ordered.append(int(c))

Li1 = [1, 10, 11, 12, 13]

# does __contains__range search the whole range or for the presence of any value in the range?
straight = 0
sf = []
if set(range(1, 6)).issubset(set(ordered)):
    straight += 1
    sf.append(1)
elif set(range(2, 7)).issubset(set(ordered)):
    straight += 1
    sf.append(2)
elif set(range(3, 8)).issubset(set(ordered)):
    straight += 1
    sf.append(3)
elif set(range(4, 9)).issubset(set(ordered)):
    straight += 1
    sf.append(4)
elif set(range(5, 10)).issubset(set(ordered)):
    straight += 1
    sf.append(5)
elif set(range(6, 11)).issubset(set(ordered)):
    straight += 1
    sf.append(6)
elif set(range(7, 12)).issubset(set(ordered)):
    straight += 1
    sf.append(7)
elif set(range(8, 13)).issubset(set(ordered)):
    straight += 1
    sf.append(8)
elif set(range(9, 14)).issubset(set(ordered)):
    straight += 1
    sf.append(9)
elif set(Li1).issubset(set(ordered)):
    straight += 1
    sf.append(10)
else:
    pass

# seeing if there is a flush on a full board.
Board_suits = board_suit(board_card1) + board_suit(board_card2) + board_suit(board_card3) + board_suit(board_card4) \
              + board_suit(board_card5)
All_suits = Hole_card_suits + Board_suits
flush = 0
if (All_suits.count("h") == 5) or (All_suits.count("h") == 6) or (All_suits.count("h") == 7) or \
   (All_suits.count("s") == 5) or (All_suits.count("s") == 6) or (All_suits.count("s") == 7) or \
   (All_suits.count("c") == 5) or (All_suits.count("c") == 6) or (All_suits.count("c") == 7) or \
   (All_suits.count("d") == 5) or (All_suits.count("d") == 6) or (All_suits.count("d") == 7):
    flush = 1
else:
    flush = 0

# def straight flush
new_suits = []


def match_list(range_cards, order, suits):
    if set(range_cards).issubset(set(order)):
        for n in range_cards:
            new_suits.append(suits[order.index(n)])
        return new_suits
    else:
        pass

match_list(range(1, 6), ordered, All_suits)
match_list(range(2, 7), ordered, All_suits)
match_list(range(3, 8), ordered, All_suits)
match_list(range(4, 9), ordered, All_suits)
match_list(range(5, 10), ordered, All_suits)
match_list(range(6, 11), ordered, All_suits)
match_list(range(7, 12), ordered, All_suits)
match_list(range(8, 13), ordered, All_suits)
match_list(range(9, 14), ordered, All_suits)
match_list(Li1, ordered, All_suits)

sf_count = []
if len(new_suits) >= 1:
    for l in new_suits:
        if l == "h":
            sf_count.append(1)
        if l == "d":
            sf_count.append(2)
        if l == "s":
            sf_count.append(3)
        if l == "c":
            sf.append(4)

straight_flush = 0

sf1 = [1, 1, 1, 1, 1]
sf2 = [2, 2, 2, 2, 2]
sf3 = [3, 3, 3, 3, 3]
sf4 = [4, 4, 4, 4, 4]

if set(sf1).issubset(set(sf_count)) or set(sf2).issubset(set(sf_count)) or set(sf3).issubset(set(sf_count)) or \
   set(sf1).issubset(set(sf_count)):
    straight_flush = 1

# def royal flush
royal_flush = 0
if (straight_flush == 1) and set(Li1).issubset(set(ordered)):
    royal_flush = 1

"""
** create a new list -- with cards foloweed by suits as a seperate value like a,h,k,h.
** Then create a new search for the straight range with a gap like (2,12,2) with a new condition that range(3,13,2)
   must have "hhhhh" or "ddddd" or "ccccc" or "sssss".

def straight_flush_present(sf, All_suits)
    if sf__contains__(1) and
"""


# Identify the strongest hand
def strongest_hand():
    if royal_flush == 1:
        print "you have a royal flush!!"
    elif straight_flush == 1:
        print "you have a straight flush!"
    elif quads == 1:
        print "you have quads!"
    elif full_house == 1:
        print "you have a full house"
    elif flush == 1:
        print "you have a flush!"
    elif straight >= 1:
        print "you have a straight!"
    elif trips == 1:
        print "you have trips!"
    elif two_pair is True:
        print "you have a two pair hand!"
    elif pair == 1:
        print "you have a pair!"
    else:
        print "you have a high card :/, best fold"


print strongest_hand()
print All_suits
print Full_board_no_suits
print ordered
print new_suits
print "y"
print "x"
