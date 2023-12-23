from aoc import Day


class Block:
    N = 0

    def __init__(self, s):
        self.block_id = Block.N
        Block.N += 1
        self.z_loc = 0
        self.s_x = s[0][0]
        self.s_y = s[0][1]
        self.s_z = s[0][2]

        self.e_x = s[1][0]
        self.e_y = s[1][1]
        self.e_z = s[1][2]

        self.nodes_above = []
        self.nodes_below = []

    def add_node_above(self, node):
        if node not in self.nodes_above:
            self.nodes_above.append(node)

    def add_node_below(self, node):
        if node not in self.nodes_below:
            self.nodes_below.append(node)

    def get_data(self) -> tuple:
        return self.s_x, self.s_y, self.s_z, self.e_x, self.e_y, self.e_z

    def get_min_x(self) -> int:
        return min(self.e_x, self.s_x)

    def get_max_x(self) -> int:
        return max(self.e_x, self.s_x)

    def get_max_y(self) -> int:
        return max(self.e_y, self.s_y)

    def get_min_y(self) -> int:
        return min(self.e_y, self.s_y)

    def get_min_z(self) -> int:
        return min(self.e_z, self.s_z)

    def __str__(self):
        return f"{self.block_id} - {self.s_x},{self.s_y},{self.s_z}~{self.e_x},{self.e_y},{self.e_z} on_top: {len(self.nodes_above)}"

class Day22(Day):

    def __init__(self):
        super().__init__(22)

    def part_one(self, raw_data: str) -> str:
        blocks = [Block([list(map(int, x.split(','))) for x in row.split('~')]) for row in raw_data.splitlines()]

        blocks.sort(key=lambda x: x.get_min_z())
        min_x = min(map(lambda x: x.get_min_x(), blocks))
        max_x = max(map(lambda x: x.get_max_x(), blocks))

        min_y = min(map(lambda x: x.get_min_y(), blocks))
        max_y = max(map(lambda x: x.get_max_y(), blocks))

        x_len = max_x - min_x + 1
        y_len = max_y - min_y + 1

        height_map = [[0] * x_len for _ in range(y_len)]

        location_map = {}

        for block in blocks:
            block: Block
            s_x, s_y, s_z, e_x, e_y, e_z = block.get_data()
            _x_len, _y_len, _z_len = e_x - s_x + 1, e_y - s_y + 1, e_z - s_z + 1

            max_z_value = 0
            for _x in range(s_x, e_x + 1):
                for _y in range(s_y, e_y + 1):
                    max_z_value = max(height_map[_y][_x], max_z_value)
            block.z_loc = max_z_value

            for _x in range(s_x, e_x + 1):
                for _y in range(s_y, e_y + 1):
                    for _z in range(max_z_value, max_z_value + _z_len):
                        location_map[(_x, _y, _z)] = block

                    if (_x, _y, max_z_value - 1) in location_map:
                        location_map[(_x, _y, max_z_value - 1)].add_node_above(block)
                        block.add_node_below(location_map[(_x, _y, max_z_value - 1)])
                    height_map[_y][_x] = max_z_value + _z_len

            # [print(''.join(map(str, row))) for row in height_map]
            # print()

        counter = 0

        for block in blocks:
            all_other_support = True
            for a_block in block.nodes_above:
                a_block: Block
                if len(a_block.nodes_below) > 1:
                    all_other_support = all_other_support and True
                else:
                    all_other_support = all_other_support and False
            if all_other_support:
                counter += 1

        return str(counter)

    def part_two(self, raw_data: str) -> str:
        blocks = [Block([list(map(int, x.split(','))) for x in row.split('~')]) for row in raw_data.splitlines()]

        blocks.sort(key=lambda x: x.get_min_z())
        min_x = min(map(lambda x: x.get_min_x(), blocks))
        max_x = max(map(lambda x: x.get_max_x(), blocks))

        min_y = min(map(lambda x: x.get_min_y(), blocks))
        max_y = max(map(lambda x: x.get_max_y(), blocks))

        x_len = max_x - min_x + 1
        y_len = max_y - min_y + 1

        height_map = [[0] * x_len for _ in range(y_len)]

        location_map = {}

        for block in blocks:
            block: Block
            s_x, s_y, s_z, e_x, e_y, e_z = block.get_data()
            _x_len, _y_len, _z_len = e_x - s_x + 1, e_y - s_y + 1, e_z - s_z + 1

            max_z_value = 0
            for _x in range(s_x, e_x + 1):
                for _y in range(s_y, e_y + 1):
                    max_z_value = max(height_map[_y][_x], max_z_value)
            block.z_loc = max_z_value

            for _x in range(s_x, e_x + 1):
                for _y in range(s_y, e_y + 1):
                    for _z in range(max_z_value, max_z_value + _z_len):
                        location_map[(_x, _y, _z)] = block

                    if (_x, _y, max_z_value - 1) in location_map:
                        location_map[(_x, _y, max_z_value - 1)].add_node_above(block)
                        block.add_node_below(location_map[(_x, _y, max_z_value - 1)])
                    height_map[_y][_x] = max_z_value + _z_len

            # [print(''.join(map(str, row))) for row in height_map]
            # print()

        counter = 0
        critical_blocks = []

        for block in blocks:
            all_other_support = True
            for a_block in block.nodes_above:
                a_block: Block
                if len(a_block.nodes_below) > 1:
                    all_other_support = all_other_support and True
                else:
                    all_other_support = all_other_support and False
            if not all_other_support:
                critical_blocks.append(block)
        print(len(blocks), len(critical_blocks))
        values = []

        for b_idx, block in enumerate(critical_blocks):
            print(f"\r{b_idx}", end="")
            falling_blocks = []
            next_blocks = block.nodes_above
            expansion = True
            while expansion:
                new_falling_blocks = []

                for n_b in next_blocks:
                    n_b: Block
                    if len(n_b.nodes_below) == 1 or all([node_below in falling_blocks for node_below in n_b.nodes_below]):
                        falling_blocks.append(n_b)
                        for nn in n_b.nodes_above:
                            if nn not in falling_blocks and nn not in new_falling_blocks:
                                new_falling_blocks.append(nn)

                next_blocks = new_falling_blocks
                expansion = len(new_falling_blocks) > 0
            values.append(len(set(falling_blocks)))
        print(sorted(values, reverse=True))
        return str(sum(values))


if __name__ == '__main__':
    # 79144
    Day22().run(False, False, True)