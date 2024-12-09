from itertools import combinations

from prometheus_client.decorator import append

from aoc import Day


class Fragment:

    def __init__(
            self,
            index: int,
            file_id: int,
            length: int,
            free: bool
    ):
        self.index = index
        self.file_id = file_id
        self.length = length
        self.free = free

    def __lt__(self, other):
        return self.index < other.index

    def __str__(self):
        if self.free:
            return '.' * self.length
        return str(self.file_id) * self.length

    def __eq__(self, other):
        return self.index == other.index and self.file_id == other.file_id

    def check_sum(self) -> int:
        if self.free:
            return 0
        return sum(map(lambda x: x * self.file_id, range(self.index, self.index + self.length)))

class Day09(Day):

    def __init__(self):
        super().__init__(year=2024, day=9)

    def _create_fragments(self, data) -> list:
        elements = list(map(int, data))

        fgs = []

        current_index = 0

        for c_idx, element in enumerate(elements):
            is_free = c_idx % 2 == 1
            fg = Fragment(
                index=current_index,
                file_id=c_idx // 2,
                length=element,
                free=is_free
            )
            current_index += element
            fgs.append(fg)

        return fgs

    def part_one(self, data: str):
        fgs = self._create_fragments(data)

        while len(list(filter(lambda x: x.free, fgs))) > 0:
            print(f"\r{len(fgs)}, {sum(map(lambda x: x.length, list(filter(lambda x: x.free, fgs))))}", end="")
            element = fgs.pop()
            if element.free:
                continue
            first_empty = list(filter(lambda x: x.free, fgs))[0]
            first_empty_idx = fgs.index(first_empty)
            empty_element = fgs.pop(first_empty_idx)

            if len(list(filter(lambda x: x.free, fgs))) == 0:
                element.index = fgs[-1].index + fgs[-1].length
                fgs.append(element)
                continue

            element.index = empty_element.index
            if element.length < empty_element.length:
                empty_element.index += element.length
                empty_element.length -= element.length
                fgs.append(empty_element)

            elif element.length > empty_element.length:

                last_not_free = list(filter(lambda x: not x.free, fgs))[-1]

                remainder_fg = Fragment(
                    index=last_not_free.index + last_not_free.length,
                    file_id=element.file_id,
                    length=element.length - empty_element.length,
                    free=False
                )
                element.length = empty_element.length
                fgs.append(remainder_fg)
                element.index = empty_element.index

            fgs.append(element)
            fgs.sort(key=lambda x: x.index)

        print()
        return f"{sum(map(lambda x: x.check_sum(), fgs))}"


    def _find_free_spot(self, fgs: list, idx: int, length: int) -> Fragment:
        fgs = list(filter(lambda x: x.free and x.length >= length and x.index < idx, fgs))
        if len(fgs) > 0:
            return fgs[0]
        return None

    def _consolidate_fragments(self, fgs) -> list:
        change_happen = True
        last_start_idx = 0
        while change_happen:
            change_happen = False
            counter = 0
            for fg_1, fg_2 in zip(fgs[last_start_idx:-1], fgs[last_start_idx + 1:]):
                if fg_1.free and fg_2.free:
                    fgs.remove(fg_2)
                    fg_1.length += fg_2.length
                    change_happen = True
                    break
                counter += 1
            last_start_idx += counter
        return fgs

    def part_two(self, data: str):
        fgs = self._create_fragments(data)

        file_ids = sorted(list(range(1, max(map(lambda x: x.file_id, fgs)) + 1)), reverse=True)

        for idx, file_id in enumerate(file_ids):
            print(f"\r{idx} / {len(file_ids)}", end="")
            file_id_idx = fgs.index(list(filter(lambda x: x.file_id == file_id, fgs))[0])
            element: Fragment = fgs.pop(file_id_idx)

            if len(list(filter(lambda x: x.free, fgs))) == 0:
                fgs.append(element)
                break

            if free_fragment := self._find_free_spot(fgs, element.index, element.length):
                left_most_free_idx = fgs.index(free_fragment)
                left_most_fragment = fgs.pop(left_most_free_idx)

                if left_most_fragment.length > element.length:
                    moved_fragment = Fragment(
                        index=left_most_fragment.index,
                        file_id=element.file_id,
                        length=element.length,
                        free=False
                    )
                    remaining_free_fragment = Fragment(
                        index=moved_fragment.index + moved_fragment.length,
                        file_id=-1,
                        length=left_most_fragment.length - element.length,
                        free=True
                    )
                    new_remaining_fragment = Fragment(
                        index=element.index,
                        file_id=-1,
                        length=element.length,
                        free=True
                    )
                    fgs.append(new_remaining_fragment)
                    fgs.append(remaining_free_fragment)
                    fgs.append(moved_fragment)


                elif left_most_fragment.length == element.length:
                    element.index, left_most_fragment.index = left_most_fragment.index, element.index

                    fgs.append(left_most_fragment)
                    fgs.append(element)

                fgs.sort()
                fgs = self._consolidate_fragments(fgs)

            else:
                fgs.append(element)
            fgs.sort()
        print()

        return f"{sum(map(lambda x: x.check_sum(), fgs))}"

    # 6389911791746

if __name__ == '__main__':
    Day09().run(demo=False, part_one=False, part_two=True)
