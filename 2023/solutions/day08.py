from aoc import Day
from math import lcm


class Day08(Day):

    def __init__(self):
        super().__init__(8)

    def part_one(self, raw_data: str) -> str:
        instructions, rows = raw_data.split("\n\n")
        directions = {}

        current_node = "AAA"

        for row in rows.splitlines():
            origin, rest = row.split(" = ")
            node_directions = rest.replace("(", "").replace(")", "").split(", ")
            directions[origin] = node_directions

        counter = 0
        while current_node != "ZZZ":
            next_step = instructions[counter % len(instructions)]
            current_node = directions[current_node][0 if next_step == 'L' else 1]
            counter += 1
        return str(counter)

    def part_two(self, raw_data: str) -> str:
        instructions, rows = raw_data.split("\n\n")
        directions = {}

        for row in rows.splitlines():
            origin, rest = row.split(" = ")
            node_directions = rest.replace("(", "").replace(")", "").split(", ")
            directions[origin] = node_directions

        current_nodes = list(filter(lambda x: x[-1] == 'A', directions.keys()))

        counter = 0

        node_steps_to_z = [-1 for _ in range(len(current_nodes))]

        while not self.all_nodes_with_z(current_nodes) and not all(list(map(lambda x: x != -1, node_steps_to_z))):
            next_step = instructions[counter % len(instructions)]
            for node_idx, node in enumerate(current_nodes):
                current_nodes[node_idx] = directions[node][0 if next_step == 'L' else 1]
                if current_nodes[node_idx][-1] == 'Z' and node_steps_to_z[node_idx] == -1:
                    node_steps_to_z[node_idx] = counter + 1

            counter += 1
        return str(lcm(*node_steps_to_z))

    def all_nodes_with_z(self, input_list: list[str]) -> bool:
        return all(list(map(lambda x: x[-1] == 'Z', input_list)))


if __name__ == '__main__':
    Day08().run()