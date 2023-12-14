from aoc import Day
from functools import cache

class Day12(Day):

    def __init__(self):
        super().__init__(12)
        self.cache = {}

    def dp(self, pattern, groups, pattern_idx, group_idx, current_len):
        key = (pattern_idx, group_idx, current_len)
        if key in self.cache.keys():
            return self.cache[key]
        if pattern_idx == len(pattern):
            if group_idx == len(groups) and current_len == 0:
                return 1
            elif group_idx == len(groups) - 1 and groups[group_idx] == current_len:
                return 1
            else:
                return 0
        result = 0
        for c in ['.', '#']:

            if pattern[pattern_idx] in f'{c}?':
                if c == '.' and current_len == 0:
                    result += self.dp(pattern, groups, pattern_idx + 1, group_idx, 0)
                elif c == '.' and current_len > 0 and group_idx < len(groups) and groups[group_idx] == current_len:
                    result += self.dp(pattern, groups, pattern_idx + 1, group_idx + 1, 0)
                elif c == '#':
                    result += self.dp(pattern, groups, pattern_idx + 1, group_idx, current_len + 1)
        self.cache[key] = result
        return result

    def count_hashes(self, input_str) -> int:
        return sum(list(map(lambda x: 1 if x == '#' else 0, input_str)))

    def recursion(self, pattern, groups, pattern_idx, group_idx, current_len):
        """
        This is a mess...
        """
        key = (pattern, pattern_idx, current_len)
        if key in self.cache.keys():
            return self.cache[key]
        if pattern_idx == len(pattern) or len(groups) == group_idx:
            if group_idx == len(groups):
                return 1 if self.count_hashes(pattern) == sum(groups) else 0
            elif group_idx == len(groups) - 1 and groups[group_idx] == current_len:
                return 1 if self.count_hashes(pattern) == sum(groups) else 0
            else:
                return 0

        if current_len == groups[group_idx]:
            if pattern[pattern_idx] == '.':
                return self.recursion(pattern, groups, pattern_idx + 1, group_idx + 1, 0)
            elif pattern[pattern_idx] == '?':
                return self.recursion(pattern[:pattern_idx] + '.' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx + 1, 0)
            elif pattern[pattern_idx] == '#':
                return 0
        elif current_len > groups[group_idx]:
            return 0

        if pattern[pattern_idx] == '.':
            if current_len == 0:
                return self.recursion(pattern, groups, pattern_idx + 1, group_idx, 0)
            elif current_len > 0 and group_idx < len(groups) and groups[group_idx] == current_len:
                return self.recursion(pattern, groups, pattern_idx + 1, group_idx + 1, 0)
        elif pattern[pattern_idx] == '#':
            return self.recursion(pattern, groups, pattern_idx + 1, group_idx, current_len + 1)
        elif pattern[pattern_idx] == '?':
            value = self.recursion(pattern[:pattern_idx] + '#' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx, current_len + 1)
            new_group = 1 if pattern_idx > 0 and pattern[pattern_idx - 1] == '#' else 0
            if current_len != 0 and current_len < groups[group_idx]:
                value += 0
            else:
                value += self.recursion(pattern[:pattern_idx] + '.' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx + new_group, 0)
                self.cache[key] = value
            return value
        return 0

    def part_one(self, raw_data: str) -> str:
        lines = [(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in raw_data.splitlines()]

        values = []

        for pattern, groups in lines:
            values.append(self.recursion(pattern, groups, 0, 0, 0))

        return str(sum(values))

    def part_two(self, raw_data: str) -> str:
        lines = [(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in raw_data.splitlines()]

        values = []

        for index, (pattern, groups) in enumerate(lines):
            pattern = '?'.join([pattern] * 5)
            groups = groups * 5
            values.append(self.dp(pattern, groups, 0, 0, 0))
            self.cache.clear()
        return str(sum(values))

        pass


if __name__ == '__main__':
    Day12().run(False, False, True)