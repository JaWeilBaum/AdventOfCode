import re
from operator import mul

def main():

    with open("in_data/day_03.txt") as f:
        data = f.read()

    part_one(data)
    part_two(data)


def part_one(raw_data: str):

    matrix = [list(row) for row in raw_data.splitlines()]

    def _check_if_adjacent_in_matrix(y: int, x_start: int, x_end: int) -> bool:
        symbols = "1234567890."
        for y in [y - 1, y, y + 1]:
            if y < 0 or y > len(matrix) - 1:
                continue
            for x in range(x_start - 1, x_end + 1):
                if x < 0 or x > len(matrix[0]) - 1:
                    continue
                if matrix[y][x] not in symbols:
                    return True
        return False


    valid_part_numbers = []

    for row_idx, row in enumerate(raw_data.splitlines()):
        reiter = re.finditer(r"\d+", row)

        for result in reiter:
            adj_result = _check_if_adjacent_in_matrix(row_idx, result.start(), result.end())
            # print(f"{result.group()}, {adj_result}")
            if adj_result:
                valid_part_numbers.append(int(result.group()))

    print(sum(valid_part_numbers))
    pass


def part_two(raw_data: str):
    matrix = [list(row) for row in raw_data.splitlines()]
    adj_list = []

    def _check_if_in_list(x: int, y: int) -> int:
        matching_list = list(filter(lambda element: element.get('x') == x and element.get('y') == y, adj_list))
        if len(matching_list) == 0:
            return -1
        return matching_list[0].get('index')

    def _check_for_gear(number: int, y: int, x_start: int, x_end: int) -> bool:

        for y in [y - 1, y, y + 1]:
            if y < 0 or y > len(matrix) - 1:
                continue
            for x in range(x_start - 1, x_end + 1):
                if x < 0 or x > len(matrix[0]) - 1:
                    continue
                if matrix[y][x] == '*':
                    element_idx = _check_if_in_list(x, y)
                    if element_idx > -1:
                        adj_list[element_idx]['values'].append(number)
                    else:
                        adj_list.append({'x': x, 'y': y, 'values': [number], 'index': len(adj_list)})
                    return True
        return False

    for row_idx, row in enumerate(raw_data.splitlines()):
        reiter = re.finditer(r"\d+", row)

        for result in reiter:
            _check_for_gear(int(result.group()), row_idx, result.start(), result.end())

    valid_part_numbers = list(map(lambda element: element.get('values')[0] * element.get('values')[1] if len(element.get('values')) > 1 else 0, adj_list))

    print(sum(valid_part_numbers))
    pass


if __name__ == '__main__':
    main()