from functools import cmp_to_key
from aoc import Day

class Day05(Day):

    def __init__(self):
        super().__init__(year=2024, day=5)

    def _is_update_valid(self, rules: list, update: list) -> bool:
        all_contain = True
        for elem_1, elem_2 in zip(update[:-1], update[1:]):

            all_contain &= rules.__contains__((elem_1, elem_2))

            if not all_contain:
                break
        return all_contain

    def _eval_updates(self, updates: list, rules: list) -> (list, list):
        valid_updates = []
        invalid_updates = []
        for update in updates:
            if self._is_update_valid(rules, update):
                valid_updates.append(update)
            else:
                invalid_updates.append(update)
        return valid_updates, invalid_updates

    def _parse_data(self, data: str) -> (list, list):
        rules, updates = data.split("\n\n")

        rules = [tuple(map(int, x.split("|"))) for x in rules.split("\n")]

        updates = [list(map(int, x.split(","))) for x in updates.split("\n")]
        return rules, updates

    def part_one(self, data: str):
        rules, updates = self._parse_data(data)

        valid_updates, _ = self._eval_updates(updates, rules)

        middle_pages_numbers = [u[len(u) // 2] for u in valid_updates]
        return f"{sum(middle_pages_numbers)}"

    def part_two(self, data: str):
        rules, updates = self._parse_data(data)
        _, invalid_updates = self._eval_updates(updates, rules)

        rules_d = {}

        for rule in rules:
            if rule[0] in rules_d:
                rules_d[rule[0]].add(rule[1])
            else:
                rules_d[rule[0]] = {rule[1]}

            if rule[1] not in rules_d:
                rules_d[rule[1]] = set()

        valid_updates = []
        for update in invalid_updates:
            fixed_update = sorted(update, key=cmp_to_key(lambda x, y: 1 if y in rules_d[x] else -1))
            valid_updates.append(fixed_update)
        middle_pages_numbers = [u[len(u) // 2] for u in valid_updates]
        return f"{sum(middle_pages_numbers)}"
        pass

if __name__ == '__main__':
    Day05().run(demo=False, part_one=False, part_two=True)
