import math


def main():

    with open("in_data/day_06.txt") as f:
        data = f.read()

    part_one(data)
    part_two(data)


def mul(input_data: list[int]) -> int:
    return_value = input_data[0]
    for value in input_data[1:]:
        return_value = return_value * value
    return return_value


def parse_row(line: str) -> list[int]:
    _, content = line.split(":")
    content = content.strip()

    return_list = []

    for element in content.split(" "):
        if len(element) == 0:
            continue
        return_list.append(int(element))
    return return_list


def parse_row_special(line: str) -> list[int]:
    _, content = line.split(":")
    content = content.replace(" ", "")

    return_list = []

    for element in content.split(" "):
        if len(element) == 0:
            continue
        return_list.append(int(element))
    return return_list


def get_xs(time, distance) -> tuple:
    """
    x_1/x_2 = (-b +- sqrt(-b^2 - 4 * a * c)) / 2 * a
    a = 1
    b = time * -1
    c = distance
    """
    time *= -1
    dis = math.sqrt((time ** 2) - 4 * distance)
    x_1 = ((-1 * time) - dis) / 2
    x_2 = ((-1 * time) + dis) / 2
    return x_1, x_2


def part_one(raw_data: str):
    times, distances = [parse_row(line) for line in raw_data.splitlines()]
    values = []

    for time, distance in zip(times, distances):
        x_1, x_2 = get_xs(time, distance)

        lower_bound = int(x_1) + 1
        upper_bound = int(x_2) - (1 if int(x_2) == x_2 else 0)

        possibilities = upper_bound - lower_bound + 1
        values.append(possibilities)
        print(f"[{lower_bound};{upper_bound}]{possibilities=}")

    print(mul(values))


def part_two(raw_data: str):
    times, distances = [parse_row_special(line) for line in raw_data.splitlines()]
    values = []

    for time, distance in zip(times, distances):
        x_1, x_2 = get_xs(time, distance)

        lower_bound = int(x_1) + 1
        upper_bound = int(x_2) - (1 if int(x_2) == x_2 else 0)

        possibilities = upper_bound - lower_bound + 1
        values.append(possibilities)
        print(f"[{lower_bound};{upper_bound}] {possibilities=}")
    print(mul(values))


if __name__ == '__main__':
    main()