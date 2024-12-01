from abc import ABC, abstractmethod
from pathlib import Path


class Day(ABC):

    def __init__(self, day: int, year: int=2023):
        self.year = str(year)
        self.day = f"{day:0>2}"
        self.file_name = f"day_{self.day}.txt"
        self.demo_file_name = f"day_{self.day}_demo.txt"
        self.base_path = Path(__file__).parent

        self.file_content = self.load_file(self.file_name)
        self.demo_file_content = self.load_file(self.demo_file_name)


    def __str__(self) -> str:
        return f"Day {self.day}"

    def load_file(self, name: str) -> str:
        with open(self.base_path.parent / self.year / "in_data" / name) as f:
            return f.read()

    def p1(self) -> str:
        return self.part_one(self.file_content)

    def p2(self) -> str:
        return self.part_two(self.file_content)

    @abstractmethod
    def part_one(self, raw_data: str) -> str:
        pass

    @abstractmethod
    def part_two(self, raw_data: str) -> str:
        pass

    def run(self, demo: bool = False, part_one: bool = True, part_two: bool = True):
        content = self.demo_file_content if demo else self.file_content
        if part_one:
            print(f"Part one: {self.part_one(content)}")
        else:
            print("Part one skipped")
        if part_two:
            print(f"Part two: {self.part_two(content)}")
        else:
            print("Part two skipped")