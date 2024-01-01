import math

from aoc import Day
from collections import deque
from copy import copy
import networkx as nx
import matplotlib.pyplot as plt

class Day20(Day):

    def __init__(self):
        super().__init__(20)
        self.modules = {}

    def parse_module(self, module_str) -> (str, dict):
        name, destination = module_str.split(' -> ')
        destinations = destination.split(', ')
        module = {}
        if '%' in name:
            module["type"] = 'f'
            module["isOn"] = False
        elif '&' in name:
            module["type"] = 'c'
        else:
            module["type"] = 'b'
        module["destinations"] = destinations
        return name.replace('%', '').replace('&', ''), module

    def create_memory(self):
        kvs = list(filter(lambda x: x[1]["type"] == 'c', self.modules.items()))

        for key, value in kvs:
            incoming = list(filter(lambda x: key in x[1]["destinations"], self.modules.items()))
            incoming_keys = list(map(lambda x: x[0], incoming))

            self.modules[key]["memory"] = {k: 'l' for k in incoming_keys}

    def process_flip_flop(self, pulse: str, target_module: str) -> list:
        # print('>' * 5 + f' -{pulse}-> {target_module} [isOn: {self.modules[target_module]["isOn"]}]')
        if pulse == 'h':
            return []

        self.modules[target_module]["isOn"] = not self.modules[target_module]["isOn"]


        if self.modules[target_module]["isOn"]:
            pulse = 'h'
        else:
            pulse = 'l'

        return list(map(lambda x: (pulse, x), self.modules[target_module]["destinations"]))

    def process_conjunction(self, pulse: str, origin_module: str, target_module: str) -> list:
        self.modules[target_module]["memory"][origin_module] = pulse

        memory_values = self.modules[target_module]["memory"].values()
        # print('>' * 5 + f' {origin_module} -{pulse}-> {target_module} == {memory_values}')
        if all(map(lambda x: x == 'h', memory_values)):
            pulse = 'l'
        else:
            pulse = 'h'
        return list(map(lambda x: (pulse, x), self.modules[target_module]["destinations"]))


    def press_button(self, _input: tuple) -> (int, int):
        l, h = 0, 0
        queue = deque()

        queue.append(_input)
        while len(queue) > 0:
            prev_node, pulse, next_node = queue.popleft()
            # print(f"{prev_node} -{pulse}-> {next_node}")
            if pulse == 'l':
                l += 1
            else:
                h += 1
            if next_module := self.modules.get(next_node):
                new_queue_values = []
                if next_module["type"] == 'b':
                    new_queue_values = list(map(lambda x: (next_node, pulse, x), self.modules[next_node]['destinations']))
                elif next_module["type"] == 'f':
                    new_queue_values = list(map(lambda x: (next_node, *x), self.process_flip_flop(pulse, next_node)))
                elif next_module["type"] == 'c':
                    new_queue_values = list(map(lambda x: (next_node, *x), self.process_conjunction(pulse, prev_node, next_node)))

                for v in new_queue_values:
                    if v[-1] == 'kj' and v[1] == 'h':
                        # print(f"FOUND!! ({_input})")
                        return -1, -1
                    queue.append(v)


        return l, h


    def part_one(self, raw_data: str) -> str:
        self.modules = {key: value for key, value in map(self.parse_module, raw_data.splitlines())}
        self.create_memory()
        # self.modules["rx"] = {"type": "", "destinations": []}
        l = 0
        h = 0

        for i in range(1_000):
            # print(f"Pressing button {i + 1}")
            _l, _h = self.press_button(('button', 'l', 'broadcaster'))
            l += _l
            h += _h

        return str(l * h)

    def lcm(self, values: list[int]) -> int:
        ans = 1
        for v in values:
            ans = (ans * v) // math.gcd(v, ans)
        return ans

    def part_two(self, raw_data: str) -> str:
        self.modules = {key: value for key, value in map(self.parse_module, raw_data.splitlines())}
        self.create_memory()

        safe_modules = copy(self.modules)

        l = 0
        h = 0
        values = []
        for start_node in self.modules['broadcaster']['destinations']:
            counter = 0
            self.modules = copy(safe_modules)
            while True:
                counter += 1
                _l, _h = self.press_button(('button', 'l', start_node))
                if _l == -1 and _h == -1:
                    # print(f"{start_node} {counter=} {l=} {h=}")
                    values.append(counter)
                    break
                else:
                    l += _l
                    h += _h
        return str(self.lcm(values))


if __name__ == '__main__':
    Day20().run(False,  False, True)