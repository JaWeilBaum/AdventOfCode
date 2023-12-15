from aoc import Day


class Day15(Day):

    def __init__(self):
        super().__init__(15)

    def hash_str(self, input_str: str) -> int:
        current_value = 0
        for letter in input_str:
            current_value += ord(letter)
            current_value *= 17
            current_value = current_value % 256
        return current_value


    def part_one(self, raw_data: str) -> str:
        values = [self.hash_str(part) for part in raw_data.split(',')]
        return str(sum(values))

    def part_two(self, raw_data: str) -> str:
        parts = [part for part in raw_data.split(',')]
        boxes = [[] for _ in range(256)]

        for part in parts:
            do_remove = part.__contains__('-')

            if do_remove:
                box_label = part.replace('-', '')
            else:
                box_label = part.split('=')[0]
            box_idx = self.hash_str(box_label)
            if do_remove:
                index_of = list(map(lambda x: x[0], filter(lambda x: x[1][0] == box_label, enumerate(boxes[box_idx]))))

                if len(index_of) == 1:
                    boxes[box_idx].pop(index_of[0])
            else:
                index_of = list(map(lambda x: x[0], filter(lambda x: x[1][0] == box_label, enumerate(boxes[box_idx]))))
                l_tuple = (box_label, int(part.split('=')[-1]))
                if len(index_of) == 1:
                    boxes[box_idx][index_of[0]] = l_tuple
                elif len(index_of) == 0:
                    boxes[box_idx].append(l_tuple)

        values = []
        for box_idx, box in enumerate(boxes):
            for slot_index, (label, focal_length) in enumerate(box):
                values.append((box_idx + 1) * (slot_index + 1) * focal_length)
        return str(sum(values))


if __name__ == '__main__':
    Day15().run(False, True, True)