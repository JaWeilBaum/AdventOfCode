from aoc import Day

class Day13(Day):

    def __init__(self):
        super().__init__(year=2024, day=13)

    def calculate(self, machine, two: bool=False) -> int:
        a_command, b_command, destination = machine.splitlines()
        ax, ay = list(map(int, a_command.replace('Button A: X', '').split(', Y')))
        bx, by = list(map(int, b_command.replace('Button B: X', '').split(', Y')))
        X, Y = list(map(int, destination.replace('Prize: X=', '').split(', Y=')))
        if two:
            X += 10000000000000
            Y += 10000000000000

        a_numerator = by * X - bx * Y
        a_denominator = ax * by - ay * bx

        b_numerator = ay * X - ax * Y
        b_denominator = bx * ay - by * ax

        if (a_numerator % a_denominator) == 0 and (b_numerator % b_denominator) == 0:
            return int(3 * (a_numerator / a_denominator) + (b_numerator / b_denominator))
        return 0

    def part_one(self, data: str):
        machines = data.split('\n\n')

        tokens = []
        for machine in machines:
            tokens.append(self.calculate(machine))
        return f"{sum(tokens)}"

    def part_two(self, data: str):
        machines = data.split('\n\n')

        tokens = []
        for machine in machines:
            tokens.append(self.calculate(machine, two=True))
        return f"{sum(tokens)}"

if __name__ == '__main__':
    Day13().run(demo=False, part_one=False, part_two=True)
