from itertools import product

from mpmath import matrix

from aoc import Day

class Day07(Day):

    def __init__(self):
        super().__init__(year=2024, day=7)

    def _get_eqs(self, data: str) -> list:
        eqs = [x.split(':') for x in data.splitlines()]
        return [(int(x[0]), list(map(int, x[1].strip().split(' ')))) for x in eqs]

    def _is_possible_two_ops(self, result: int, remaining_numbers: list, current_value: int) -> bool:
        if len(remaining_numbers) == 0 and current_value == result:
            # print(ops)
            return True

        if len(remaining_numbers) == 0 and current_value != result:
            return False

        if len(remaining_numbers) >= 0 and current_value > result:
            return False

        return any([
            self._is_possible_two_ops(result, remaining_numbers[1:], current_value * remaining_numbers[0]),
            self._is_possible_two_ops(result, remaining_numbers[1:], current_value + remaining_numbers[0]),
        ])

    def _is_possible_three_ops(self, result: int, remaining_numbers: list, current_value: int) -> bool:
        if len(remaining_numbers) == 0 and current_value == result:
            # print(ops)
            return True

        if len(remaining_numbers) == 0 and current_value != result:
            return False

        if len(remaining_numbers) >= 0 and current_value > result:
            return False

        return any([
            self._is_possible_three_ops(result, remaining_numbers[1:], current_value * remaining_numbers[0]),
            self._is_possible_three_ops(result, remaining_numbers[1:], current_value + remaining_numbers[0]),
            self._is_possible_three_ops(result, remaining_numbers[1:], (current_value * (10 ** len(str(remaining_numbers[0])))) + remaining_numbers[0]),
        ])

    def _calc(self, numbers: list, ops: list) -> int:
        result = numbers[0]
        for number, op in zip(numbers[1:], ops):
            if op == '+':
                result += number
            elif op == '*':
                result *= number
        return result

    def _eval(self, result: int, numbers: list) -> bool:
        return any([
            self._calc(numbers, ops) == result for ops in product(['+', '*'], repeat=len(numbers))
        ])

    def part_one(self, data: str):

        eqs = self._get_eqs(data)

        results = []
        for result, numbers in eqs:
            if self._is_possible_two_ops(result, numbers[1:], numbers[0]):
                results.append(result)

        return f"{sum(results)}"

    def part_two(self, data: str):
        eqs = self._get_eqs(data)

        results = []
        for result, numbers in eqs:
            if self._is_possible_three_ops(result, numbers[1:], numbers[0]):
                results.append(result)

        return f"{sum(results)}"

if __name__ == '__main__':
    Day07().run(demo=False, part_one=False, part_two=True)
