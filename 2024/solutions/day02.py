from aoc import Day


class Day02(Day):

    def __init__(self):
        super().__init__(year=2024, day=2)

    def part_one(self, data: str):

        data = [list(map(int, x.split(" "))) for x in data.splitlines()]

        valid_seqs, _ = self._split_seqs(data)

        return f"{len(valid_seqs)}"

    def _split_seqs(self, seqs: list) -> (list, list):
        valid_seqs = []
        invalid_seqs = []

        for seq in seqs:
            if self._is_seq_valid(seq):
                valid_seqs.append(seq)
            else:
                invalid_seqs.append(seq)

        return valid_seqs, invalid_seqs

    def _is_seq_valid(self, seq: list) -> bool:
        dist = self._get_distances(seq)

        return all(map(lambda x: 3 >= x >= 1, dist)) or all(map(lambda x: -3 <= x <= -1, dist))

    def _get_distances(self, sequence: list) -> list:
        return [x - y for x, y in zip(sequence, sequence[1:])]

    def part_two(self, data: str):

        data = [list(map(int, x.split(" "))) for x in data.splitlines()]
        valid_seqs, invalid_seqs = self._split_seqs(data)

        for seq in invalid_seqs:

            if any([self._is_seq_valid(_seq) for _seq in [seq[:x] + seq[x+1:] for x in range(len(seq))]]):
                valid_seqs.append(seq)

        return f"{len(valid_seqs)}"

if __name__ == '__main__':
    Day02().run(demo=False, part_one=False, part_two=True)
