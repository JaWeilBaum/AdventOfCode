import math
from multiprocessing import Pool

import numpy as np
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


def part_two(raw_data: str):
    # Just rewrite the ranges and split ranges if overlap occur
    rows = raw_data.split("\n\n")
    seeds = parse_row(rows[0].replace("seeds: ", ""))

    value_groups = list(zip(seeds[::2], seeds[1::2]))
    value_groups = [(x[0], sum(x)) for x in value_groups]

    for idx, row in enumerate(rows[1:]):
        ranges = list(map(parse_row, row.splitlines()[1:]))

        new_value_groups = []
        while len(value_groups) > 0:
            start, end = value_groups.pop()

            for destination_start, source_start, range_length in ranges:
                # Check overlap
                overlap_start = max(start, source_start)
                overlap_end = min(end, source_start + range_length)
                if overlap_start < overlap_end:
                    # Overlap is not empty as the start is smaller than the end
                    new_value_groups.append((overlap_start - source_start + destination_start, overlap_end - source_start + destination_start))
                    if overlap_start > start:
                        value_groups.append((start, overlap_start))
                    if end > overlap_end:
                        value_groups.append((overlap_end, end))
                    break
            else:
                new_value_groups.append((start, end))
        value_groups = new_value_groups

    print(min(value_groups)[0])


if __name__ == '__main__':
    main()