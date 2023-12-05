from multiprocessing import Pool
from tqdm import tqdm

def main():

    with open("in_data/day_05.txt") as f:
        data = f.read()

    part_one(data)
    part_two(data)


def parse_row(row: str) -> list[int]:
    return [int(element) for element in row.split(" ")]


def create_map(data: str) -> list[dict]:
    rows = data.splitlines()
    range_rows = [parse_row(row) for row in rows[1:]]
    mappings = []

    for destination_range_start, source_range_start, range_length in range_rows:
        mappings.append({'range': [source_range_start, source_range_start + range_length], 'add_value': destination_range_start - source_range_start})
    return mappings


def map_number(number: int, mappings: list[dict]) -> int:
    for mapping in mappings:
        if mapping.get('range')[0] <= number < mapping.get('range')[1]:
            return number + mapping.get('add_value')

    return number


def part_one(raw_data: str):
    rows = raw_data.split("\n\n")
    values = parse_row(rows[0].replace("seeds: ", ""))

    for row_idx, row in enumerate(rows[1:]):
        print(row_idx)
        mapping = create_map(row)
        for value_index, value in enumerate(values):
            values[value_index] = map_number(value, mapping)

    print(min(values))


def resolve_overlap(base_mapping: list[dict], input_mapping: dict) -> list[dict]:
    """
                        0        1
    mapping             |--------|
                   0     1
    input_mapping  |-----|

    :param base_mapping:
    :param input_mapping:
    :return:
    """
    new_mappings = []
    del_index_mappings = []
    for mapping_idx, mapping in enumerate(base_mapping):
        if mapping["range"][0] > input_mapping["range"][1] or mapping["range"][1] < input_mapping["range"][0]:
            # input mapping is completely left or right of mapping
            new_mappings.append(input_mapping)
        elif mapping["range"][0] < input_mapping["range"][0] and mapping["range"][1] > input_mapping["range"][1]:
            # input mapping is completely contained in
            pass


    return base_mapping + new_mappings



def merge_mapping(base_mappings: list[dict], new_mappings: list[dict]) -> list[dict]:

    for mapping in new_mappings:
        resolve_overlap(base_mappings, mapping)
        print()


def process_range_and_mappings(pid: int, raw_input_range: tuple, mappings: list[list[dict]]) -> int:
    input_range = list(range(raw_input_range[0], raw_input_range[0] + raw_input_range[1]))
    with tqdm(total=len(mappings) * raw_input_range[1], leave=True, desc=f"PID: {pid}", position=pid + 1) as pbar:
        for mapping in mappings:
            for value_index, value in enumerate(input_range):
                input_range[value_index] = map_number(value, mapping)
                pbar.update(1)

    return min(input_range)

def part_two(raw_data: str):
    rows = raw_data.split("\n\n")
    values = parse_row(rows[0].replace("seeds: ", ""))

    value_groups = list(zip(values[::2], values[1::2]))

    mappings = [create_map(row) for row in rows[1:]]

    args = list(zip(range(len(value_groups)), value_groups, [mappings] * len(value_groups)))

    with Pool(processes=10) as pool:

        return_values = pool.starmap(process_range_and_mappings, args)
        print(min(return_values))
    # values = process_range_and_mappings(0, value_groups[0], mappings)


    print(min(values))


if __name__ == '__main__':
    main()
    # print(resolve_overlap([{'add_value': -48, 'range': [98, 100]}, {'add_value': 2, 'range': [50, 98]}], {'add_value': 0, 'range': [0, 10]}))