from aoc import Day


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
        if pulse == 'h':
            return []

        self.modules[target_module]["isOn"] = not self.modules[target_module]["isOn"]
        if self.modules[target_module]["isOn"]:
            pulse = 'h'
        else:
            pulse = 'l'

        return list(map(lambda x: (pulse, x), self.modules[target_module]["destinations"]))

    def process_conjunction(self, pulse: str, origin_module: str, target_module: str) -> list:
        self.modules[target_module]["memory"][origin_module] = 'l' if self.modules[target_module]["memory"][origin_module] != 'l' else 'h'

        memory_values = self.modules[target_module]["memory"].values()
        if all(map(lambda x: x == 'h', memory_values)):
            pulse = 'l'
        else:
            pulse = 'h'
        return list(map(lambda x: (pulse, x), self.modules[target_module]["destinations"]))



    def part_one(self, raw_data: str) -> str:
        self.modules = {key: value for key, value in map(self.parse_module, raw_data.splitlines())}
        self.create_memory()
        self.modules["output"] = {"type": "", "destinations": []}
        l = 0
        h = 0

        for i in range(1000):
            print(f"Pressing button {i + 1}")
            queue = [('button', 'l', 'broadcaster')]
            while len(queue) > 0:
                prev_node, pulse, next_node = queue.pop(0)
                new_queue_values = []
                # print(f"{prev_node} -{pulse}-> {next_node}")
                if pulse == 'l':
                    l += 1
                else:
                    h += 1
                if next_module := self.modules.get(next_node):



                    if next_module["type"] == 'b':
                        new_queue_values = list(list(map(lambda x: (next_node, pulse, x), self.modules[next_node]['destinations'])))
                    elif next_module["type"] == 'f':
                        new_queue_values = list(list(map(lambda x: (next_node, *x), self.process_flip_flop(pulse, next_node))))
                    elif next_module["type"] == 'c':
                        new_queue_values = list(list(map(lambda x: (next_node, *x), self.process_conjunction(pulse, prev_node, next_node))))

                    queue.extend(new_queue_values)

        # print(self.process_conjunction('l', 'c', 'inv'))

        print(l * h)

        pass

    def part_two(self, raw_data: str) -> str:
        pass


if __name__ == '__main__':
    # 850885266
    # To low: 735050423
    Day20().run(False,  True, False)