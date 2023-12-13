from aoc import Day


class Day12(Day):

    def __init__(self):
        super().__init__(12)

        self.DP = {}

    def _f(self, dots, blocks, i, bi, current):
        key = (i, bi, current)
        if key in self.DP:
            return self.DP[key]
        if i == len(dots):
            if bi == len(blocks) and current == 0:
                return 1
            elif bi == len(blocks) - 1 and blocks[bi] == current:
                return 1
            else:
                return 0
        ans = 0
        for c in ['.', '#']:
            if dots[i] == c or dots[i] == '?':
                if c == '.' and current == 0:
                    ans += self._f(dots, blocks, i + 1, bi, 0)
                elif c == '.' and current > 0 and bi < len(blocks) and blocks[bi] == current:
                    ans += self._f(dots, blocks, i + 1, bi + 1, 0)
                elif c == '#':
                    ans += self._f(dots, blocks, i + 1, bi, current + 1)
        self.DP[key] = ans
        return ans

    def f(self, pattern, groups, pattern_idx, group_idx, current_len):
        if pattern_idx == len(pattern) or len(groups) == group_idx:
            if group_idx == len(groups):
                return 1
            elif group_idx == len(groups) - 1 and groups[group_idx] == current_len:
                return 1
            else:
                return 0

        if current_len == groups[group_idx]:
            if pattern[pattern_idx] == '.':
                return self.f(pattern, groups, pattern_idx + 1, group_idx + 1, 0)
            elif pattern[pattern_idx] == '?':
                return self.f(pattern[:pattern_idx] + '.' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx + 1, 0)
            elif pattern[pattern_idx] == '#':
                return 0
        elif current_len > groups[group_idx]:
            return 0

        if pattern[pattern_idx] == '.':
            if current_len == 0:
                return self.f(pattern, groups, pattern_idx + 1, group_idx, 0)
            elif current_len > 0 and group_idx < len(groups) and groups[group_idx] == current_len:
                return self.f(pattern, groups, pattern_idx + 1, group_idx + 1, 0)
        elif pattern[pattern_idx] == '#':
            return self.f(pattern, groups, pattern_idx + 1, group_idx, current_len + 1)
        elif pattern[pattern_idx] == '?':
            value = self.f(pattern[:pattern_idx] + '#' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx, current_len + 1)
            new_group = 1 if pattern_idx > 0 and pattern[pattern_idx - 1] == '#' else 0
            if current_len != 0 and current_len < groups[group_idx]:
                value += 0
            else:
                value += self.f(pattern[:pattern_idx] + '.' + pattern[pattern_idx + 1:], groups, pattern_idx + 1, group_idx + new_group, 0)
            return value
        return 0

    def part_one(self, raw_data: str) -> str:
        lines = [(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in raw_data.splitlines()]

        values = []

        for pattern, groups in lines:
            print(pattern, self._f(pattern, groups, 0, 0, 0), self.f(pattern, groups, 0, 0, 0))

        print(values)
        return str(sum(values))

    def part_two(self, raw_data: str) -> str:
        pass


if __name__ == '__main__':
    Day12().run(True, True, False)