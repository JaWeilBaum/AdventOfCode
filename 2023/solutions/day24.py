from aoc import Day
from z3 import Real, Solver


class Day24(Day):

    def __init__(self):
        super().__init__(24)

    def part_one(self, raw_data: str) -> str:

        rows = [row.split(' @ ') for row in raw_data.splitlines()]

        # r_s, r_e = 7, 27
        r_s, r_e = 200_000_000_000_000, 400_000_000_000_000
        counter = 0
        for r_1_idx, (loc_1, v_1) in enumerate(rows):
            for r_2_idx, (loc_2, v_2) in enumerate(rows):
                if r_1_idx >= r_2_idx:
                    continue
                x_1, y_1, z_1 = list(map(int, loc_1.split(', ')))
                x_2, y_2, z_2 = list(map(int, loc_2.split(', ')))

                v_x_1, v_y_1, v_z_1 = list(map(int, v_1.split(', ')))
                v_x_2, v_y_2, v_z_2 = list(map(int, v_2.split(', ')))
                # print(f"{x_1}, {y_1}, {z_1} @ {v_x_1}, {v_y_1}, {v_z_1}\n{x_2}, {y_2}, {z_2} @ {v_x_2}, {v_y_2}, {v_z_2} - ", end="")

                m_1 = v_y_1 / v_x_1
                m_2 = v_y_2 / v_x_2

                b_1 = ((-1 * x_1) * m_1 + y_1)
                b_2 = ((-1 * x_2) * m_2 + y_2)

                fn_1 = lambda x: m_1 * x + b_1
                fn_2 = lambda x: m_2 * x + b_2

                bottom = m_1 - m_2

                if bottom == 0:
                    # print("Bottom == 0!\n")
                    continue

                t = (b_2 - b_1) / bottom
                if t < 0:
                    # print(f"IN PAST {t=:.2f}\n")
                    continue

                valid_A = False
                if v_x_1 > 0 and v_y_1 > 0:
                    valid_A = t > x_1 and fn_1(t) > y_1
                elif v_x_1 > 0 and v_y_1 < 0:
                    valid_A = t > x_1 and fn_1(t) < y_1
                elif v_x_1 < 0 and v_y_1 > 0:
                    valid_A = t < x_1 and fn_1(t) > y_1
                elif v_x_1 < 0 and v_y_1 < 0:
                    valid_A = t < x_1 and fn_1(t) < y_1

                valid_B = False
                if v_x_2 > 0 and v_y_2 > 0:
                    valid_B = t > x_2 and fn_1(t) > y_2
                elif v_x_2 > 0 and v_y_2 < 0:
                    valid_B = t > x_2 and fn_2(t) < y_2
                elif v_x_2 < 0 and v_y_2 > 0:
                    valid_B = t < x_2 and fn_2(t) > y_2
                elif v_x_2 < 0 and v_y_2 < 0:
                    valid_B = t < x_2 and fn_2(t) < y_2


                if r_s <= t <= r_e and r_s <= fn_1(t) <= r_e and valid_A and valid_B:
                    # print(f"IN! {t=:.2f} {fn_1(t)=:.2f}\n")
                    counter += 1
                else:
                    pass
                    # print(f"OUT! {t=:.2f} {fn_1(t)=:.2f} {valid_A=} {valid_B=}\n")

        return str(counter)

    def part_two(self, raw_data: str) -> str:
        def f(s):
            return Real(s)

        x, y, z = f('x'), f('y'), f('z')
        v_x, v_y, v_z = f('v_x'), f('v_y'), f('v_z')

        rows = [row.split(' @ ') for row in raw_data.splitlines()]

        ts = [f(f't{i}') for i in range(len(rows))]

        s = Solver()
        for row_idx, (loc, v) in enumerate(rows):
            x_c, y_c, z_c = list(map(int, loc.split(', ')))
            v_x_c, v_y_c, v_z_c = list(map(int, v.split(', ')))

            s.add(x + ts[row_idx] * v_x - x_c - ts[row_idx] * v_x_c == 0)
            s.add(y + ts[row_idx] * v_y - y_c - ts[row_idx] * v_y_c == 0)
            s.add(z + ts[row_idx] * v_z - z_c - ts[row_idx] * v_z_c == 0)

        res = s.check()
        m = s.model()
        return str(m.eval(x+y+z))


if __name__ == '__main__':
    # Too low
    # 105
    Day24().run(False, False, True)