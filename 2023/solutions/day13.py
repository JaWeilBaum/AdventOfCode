from aoc import Day


class Day13(Day):

    def __init__(self):
        super().__init__(13)

    def num_not_similar(self, a: list, b: list) -> int:
        ans = sum(list(map(lambda x: 0 if x[0] == x[1] else 1, zip(a, b))))
        return ans

    def check_vertical_mirror(self, block: list[list[str]]) -> int:
        for idx in range(1, len(block[0])):
            all_check = 0
            for row in block:
                all_check += self.num_not_similar(list(reversed(row[:idx])), row[idx:])
            if all_check == 0:
                return idx
        return -1

    def check_vertical_mirror_fix(self, block: list[list[str]]) -> int:
        for idx in range(1, len(block[0])):
            all_check = 0
            for row in block:
                all_check += self.num_not_similar(list(reversed(row[:idx])), row[idx:])
            if all_check == 1:
                return idx
        return -1

    def transpose_block(self, block: list[list[str]]) -> list[list[str]]:
        t_block = []
        for column in range(len(block[0])):
            t_block.append(list(map(lambda row: row[column], block)))
        return t_block

    def part_one(self, raw_data: str) -> str:
        blocks = raw_data.split("\n\n")

        horizontal = []
        vertical = []
        for block in blocks:
            p_block = [list(x) for x in block.splitlines()]
            t_block = self.transpose_block(p_block)

            h_value = self.check_vertical_mirror(t_block)
            if h_value != -1:
                horizontal.append(h_value)
                continue
            v_value = self.check_vertical_mirror(p_block)
            if v_value != -1:
                vertical.append(v_value)
                continue

        h_sum = sum(list(map(lambda x: x * 100, horizontal)))
        v_sum = sum(vertical)

        return str(h_sum + v_sum)

    def part_two(self, raw_data: str) -> str:
        blocks = raw_data.split("\n\n")

        horizontal = []
        vertical = []
        for block in blocks:
            p_block = [list(x) for x in block.splitlines()]
            t_block = self.transpose_block(p_block)

            h_value = self.check_vertical_mirror_fix(t_block)
            if h_value != -1:
                horizontal.append(h_value)
                continue
            v_value = self.check_vertical_mirror_fix(p_block)
            if v_value != -1:
                vertical.append(v_value)
                continue

        h_sum = sum(list(map(lambda x: x * 100, horizontal)))
        v_sum = sum(vertical)

        return str(h_sum + v_sum)


if __name__ == '__main__':
    Day13().run(False, True, True)