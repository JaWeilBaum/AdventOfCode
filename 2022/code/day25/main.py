

def main():

    with open("../../data/day_25.txt") as f:
        data = f.read()

    part_one(data)


def to_snafu(value: int) -> str:

    current_value = 0

    results = []
    remaining_elements = 100
    while current_value < value:
        print(current_value, value)
        for i in range(1, 100):
            for lower, upper in zip([-2, -1, 0, 1], [-1, 0, 1, 2]):
                if (5 ** i) * lower < value - current_value <= (5 ** i) * upper:
                    current_value += (5 ** i) * upper

                    print((5**i * 2))
                    print(i)
                    print(lower, upper)
                    results.append(upper)
                    remaining_elements = i
                    break
            break
    results += [0 for _ in range(remaining_elements)]
    print(f"{remaining_elements=}")
    print(f"{results=}")
    print(f"{current_value=}")


def parse_line(line: str) -> int:

    values = []
    for index, value in enumerate(reversed(list(line))):

        if value in "210":
            factor = int(value)
        elif value == '-':
            factor = -1
        else:
            factor = -2

        values.append((5 ** index) * factor)

    # print(values)
    # print(sum(values))
    return sum(values)


def part_one(data: str):

    values = []

    for line in data.splitlines():
        values.append(parse_line(line))

    print(sum(values))


if __name__ == '__main__':
    # parse_line("2=-01")
    to_snafu(10)
    # main()