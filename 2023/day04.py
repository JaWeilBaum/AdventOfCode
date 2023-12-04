def main():

    with open("in_data/day_04.txt") as f:
        data = f.read()

    part_one(data)
    part_two(data)


def to_list_of_int(input_str: str) -> list[int]:
    return_list = []
    for x in input_str.split(' '):
        if len(x) == 0:
            continue
        return_list.append(int(x))
    return return_list


def create_cards_with_num_matches(raw_data: str) -> list[int]:
    cards = [card.split(": ")[1].split(" | ") for card in raw_data.splitlines()]

    cards_with_numbers = [list(map(lambda x: set(to_list_of_int(x)), card)) for card in cards]

    return [len(card[0].intersection(card[1])) for card in cards_with_numbers]


def part_one(raw_data: str):
    matches = create_cards_with_num_matches(raw_data)

    points = [2 ** (x-1) if x > 0 else 0 for x in matches]

    print(sum(points))


def part_two(raw_data: str):
    matches = create_cards_with_num_matches(raw_data)
    won_cards = {x + 1: 1 for x in range(len(matches))}

    for card_index, card in enumerate(matches):
        for x in range(card):
            won_cards[card_index + 1 + 1 + x] += won_cards[card_index + 1]

    print(sum(won_cards.values()))


if __name__ == '__main__':
    main()