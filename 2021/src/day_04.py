import pandas as pd


def get_data() -> (list[pd.DataFrame], list):

    with open("files/day04_input.txt") as f:
        content = f.read()

    lines = content.split("\n")

    input_numbers = list(map(int, lines[0].split(",")))

    lines = list(filter(lambda x: len(x) > 0, lines[2:]))

    total_lines = len(lines)

    all_fields = []

    for i in range(round(total_lines / 5)):
        field = lines[i * 5:(i + 1) * 5]
        field = [list(map(int, filter(lambda y: len(y) > 0, x.split(" ")))) for x in field]
        df = pd.DataFrame(field)
        all_fields.append(df)

    return all_fields, input_numbers


def main_01():
    all_fields, input_numbers = get_data()

    for number in input_numbers:
        print(f"Number: {number}")
        for field in all_fields:
            field.replace(number, 0, inplace=True)
            sum_vertical = field.sum()
            sum_horizontal = field.sum(axis=1)

            if any(sum_vertical == 0) or any(sum_horizontal == 0):
                print(f"Solution: {sum_horizontal.sum() * number}")
                return


def main_02():
    all_fields, input_numbers = get_data()

    for number in input_numbers:
        print(f"Number: {number}")
        print(f"Fields left: {len(all_fields)}")

        index_to_pop = []

        for index, field in enumerate(all_fields):
            field.replace(number, 0, inplace=True)
            sum_vertical = field.sum()
            sum_horizontal = field.sum(axis=1)

            if any(sum_vertical == 0) or any(sum_horizontal == 0):
                print(f"Solution: {sum_horizontal.sum() * number}")
                index_to_pop.append(index)

        for counter_index, index in enumerate(index_to_pop):
            all_fields.pop(index - counter_index)

if __name__ == '__main__':
    # main_01()
    # main_02()
    pass