from aoc import Day


class Day09(Day):

    def __init__(self):
        super().__init__(9)

    def diff_row(self, values: list[int]) -> list[int]:
        return_values = []
        for a, b in zip(values[:-1], values[1:]):
            return_values.append(b - a)
        return return_values

    def part_one(self, raw_data: str) -> str:
        rows = raw_data.splitlines()
        history_values = []

        for row in rows:
            values = [int(x) for x in row.split(' ')]
            last_values = [values[-1]]
            while not all(list(map(lambda x: x == 0, values))):
                values = self.diff_row(values)
                last_values.append(values[-1])
            history_values.append(sum(last_values))

        return str(sum(history_values))

    def part_two(self, raw_data: str) -> str:
        rows = raw_data.splitlines()
        history_values = []

        for row in rows:
            values = list(reversed([int(x) for x in row.split(' ')]))
            last_values = [values[-1]]
            while not all(list(map(lambda x: x == 0, values))):
                values = self.diff_row(values)
                last_values.append(values[-1])
            history_values.append(sum(last_values))

        return str(sum(history_values))



if __name__ == '__main__':
    Day09().run(False, False, True)