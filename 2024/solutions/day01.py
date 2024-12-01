from aoc import Day


class Day01(Day):

    def __init__(self):
        super().__init__(year=2024, day=1)

    def _get_tow_cols(self, data: str):
        rows = [list(map(int, x.split("   "))) for x in data.splitlines()]
        col_1 = sorted([x[0] for x in rows])
        col_2 = sorted([x[1] for x in rows])

        return col_1, col_2

    def part_one(self, data: str):

        col_1, col_2 = self._get_tow_cols(data=data)

        distance = [abs(x_2 - x_1) for x_1, x_2 in zip(col_1, col_2)]

        return f"{sum(distance)}"

    def _create_count_dict(self, col: list) -> dict:

        base_dict = {}

        for elem in col:
            if elem not in base_dict.keys():
                base_dict[elem] = 1
            else:
                base_dict[elem] += 1

        return base_dict

    def part_two(self, data: str):

        col_1, col_2 = self._get_tow_cols(data=data)

        dict_1 = self._create_count_dict(col=col_1)
        dict_2 = self._create_count_dict(col=col_2)

        total_values = []

        for key, value in dict_1.items():
            if key not in dict_2.keys():
                continue

            total_values.append(key * value * dict_2[key])

        return f"{sum(total_values)}"


if __name__ == '__main__':
    Day01().run(demo=False, part_one=False, part_two=True)
