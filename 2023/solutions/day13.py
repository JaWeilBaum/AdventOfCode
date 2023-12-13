from aoc import Day


class Day13(Day):

    def __init__(self):
        super().__init__(13)

    def check_similar(self, a: list, b: list) -> bool:
        print(a)
        print(b)
        return all(list(map(lambda x: x[0] == x[1], zip(a, b))))

    def check_horizontal_mirror(self, block: list[list[str]]) -> int:

        for index in range(1, len(block) - 1):
            all_check = False
            if self.check_similar(block[:index][-1], block[index:][0]):
                print(f"Similar at {index} checking more")
                all_check = True
                for offset in range(len(block) - index):
                    if index <= offset:
                        break
                    result = self.check_similar(block[:index][-1 - offset], block[index:][offset])
                    print(offset, result)
                    all_check = all_check and result

            if all_check:
                return index

        return -1

    def check_vertical_mirror(self, block: list[list[str]]) -> int:

        for idx in range(1, len(block[0])):
            all_check = True
            for row in block:
                all_check = all_check and self.check_similar(list(reversed(row[:idx])), row[idx:])
            print(idx, all_check)
            if all_check:
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
            # [print(row) for row in p_block]
            # print()
            # [print(row) for row in t_block]

            h_value = self.check_vertical_mirror(t_block)
            if h_value != -1:
                horizontal.append(h_value)
                continue
            v_value = self.check_vertical_mirror(p_block)
            if v_value != -1:
                vertical.append(v_value)
                continue
            print("ERROR")

        h_sum = sum(list(map(lambda x: x * 100, horizontal)))
        v_sum = sum(vertical)

        print(h_sum + v_sum)
        pass

    def part_two(self, raw_data: str) -> str:
        pass


if __name__ == '__main__':
    Day13().run(False, True, False)