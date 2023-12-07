

def main():

    with open("in_data/day_07.txt") as f:
        data = f.read()

    part_one(data)
    part_two(data)


ORDER = "23456789TJQKA"
ADJUSTED_ORDER = "J23456789TQKA"


def count_cards(hand: str) -> dict:
    hand_dict = {}
    for card in hand:
        if card in hand_dict.keys():
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1
    return hand_dict


def get_hand_score(hand: str) -> int:
    """
    Hand order:
    - Five of a kind    AAAAA - 6
    - Four of a kind    AA8AA - 5
    - Full house        23332 - 4
    - Three of a kind   TTT98 - 3
    - Two pair          23432 - 2
    - One pair          A23A4 - 1
    - High card         23456 - 0
    """

    hand_dict = count_cards(hand)

    if len(hand_dict.keys()) == 1:
        # Five if a kind!
        return 6
    elif len(hand_dict.keys()) == 2:
        # Four of a kind OR Full house
        if max(hand_dict.values()) == 4:
            # Four of a kind
            return 5
        else:
            # Full house
            return 4
    elif max(hand_dict.values()) == 3:
        # Three of a kind
        return 3
    elif len(list(filter(lambda x: x == 2, hand_dict.values()))) == 2:
        # Two pair
        return 2
    elif len(list(filter(lambda x: x == 2, hand_dict.values()))) == 1:
        # One pair
        return 1
    else:
        # High card
        return 0


def get_adjusted_hand_score(hand: str) -> int:
    """
    Hand order:
    - Five of a kind    AAAAA - 6 check
    - Four of a kind    AA8AA - 5 check
    - Full house        23332 - 4 check
    - Three of a kind   TTT98 - 3 check
    - Two pair          23432 - 2 -> three of a kind is always better!
    - One pair          A23A4 - 1 check
    - High card         23456 - 0 -> if there is J, there always can be a better score!
    """

    hand_dict = count_cards(hand)

    num_js = hand_dict.get('J', 0)
    if num_js == 0:
        # No J's do it as before!
        return get_hand_score(hand)

    # 1 key  -> five of a kind only
    # 2 keys -> four of a kind only!
    # 3 keys -> full hose or four of a kind


    if len(hand_dict.keys()) <= 2:
        # Five if a kind! Only J's - Yes this case exists!
        # Five of a kind, as there is a J
        return 6
    elif len(hand_dict.keys()) == 3:
        # Full house and for of a kind possible
        if num_js == 1 and len(list(filter(lambda x: x == 2, hand_dict.values()))) == 2:
            # AABBJ -> Full house
            return 4
        else:
            # AAABJ -> Four of a kind
            # AABJJ -> Four of a kind
            # ABJJJ -> Four of a kind
            return 5
    elif len(hand_dict.keys()) == 4:
        # Three of a kind and Two pairs are possible, but three of a kind is always better
        # AABCJ -> Three of a kind
        # ABCJJ -> Three of a kind
        return 3
    else:
        # If there is a J, there can always be a pair!
        # ABCDJ -> One pair
        return 1


def get_hand_order(hand: str) -> int:
    output_str = ""
    for card in hand:
        card_value = ORDER.find(card)
        output_str += ('0' if len(str(card_value)) == 1 else '') + str(card_value)
    return int(output_str)


def get_adjusted_hand_order(hand: str) -> int:
    output_str = ""
    for card in hand:
        card_value = ADJUSTED_ORDER.find(card) + 1
        output_str += ('0' if len(str(card_value)) == 1 else '') + str(card_value)
    return int(output_str)


def part_one(raw_data: str):
    hands = [[x.split()[0], int(x.split()[1])] for x in raw_data.splitlines()]

    data = []

    for hand, bid in hands:
        data.append((hand, bid, get_hand_score(hand), get_hand_order(hand)))

    data = sorted(data, key=lambda x: (x[2], x[3]))

    # for index, (hand, bid, score, order) in enumerate(data):
    #     print(index, hand, score, order)

    values = [(idx + 1) * x[1] for idx, x in enumerate(data)]
    print(sum(values))
    pass


def part_two(raw_data: str):
    hands = [[x.split()[0], int(x.split()[1])] for x in raw_data.splitlines()]

    data = []

    for hand, bid in hands:
        data.append((hand, bid, get_adjusted_hand_score(hand), get_adjusted_hand_order(hand)))

    data = sorted(data, key=lambda x: (x[2], x[3]))

    # for index, (hand, bid, score, order) in enumerate(data):
    #     print(index, hand, score, order)

    values = [(idx + 1) * x[1] for idx, x in enumerate(data)]
    print(sum(values))


if __name__ == '__main__':
    main()