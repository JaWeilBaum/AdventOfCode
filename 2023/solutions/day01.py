import re
from aoc import Day


class Day01(Day):

    def __init__(self):
        super().__init__(1)

    def part_one(self, data: str):
        "".isdigit()
        rows = data.split("\n")
        rows = ["".join(list(filter(lambda x: x.isdigit(), row_values))) for row_values in rows]
        rows = [int(f"{x[0]}{x[-1]}") for x in rows]
        return str(sum(rows))

    def _replace_str_with_digit(self, input_str: str) -> [(str, int)]:
        replace_dict = {"one": "1",
                        "two": "2",
                        "three": "3",
                        "four": "4",
                        "five": "5",
                        "six": "6",
                        "seven": "7",
                        "eight": "8",
                        "nine": "9",
                        "1": "1",
                        "2": "2",
                        "3": "3",
                        "4": "4",
                        "5": "5",
                        "6": "6",
                        "7": "7",
                        "8": "8",
                        "9": "9"}

        return_list = []

        for key, value in replace_dict.items():
            res = re.finditer(rf"{key}", input_str)
            for _res in res:
                return_list.append((value, _res.start()))

        return sorted(return_list, key=lambda x: x[1])

    def part_two(self, data: str):
        total = 0
        for row in data.split("\n"):

            row_result = self._replace_str_with_digit(row)

            total += int(f"{row_result[0][0]}{row_result[-1][0]}")
        return str(total)


if __name__ == '__main__':
    Day01().run()
