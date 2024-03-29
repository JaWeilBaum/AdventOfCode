import re
from aoc import Day


class Day02(Day):

    def __init__(self):
        super().__init__(2)

    def row_to_tuple(self, input_str: str) -> list[dict]:
        res = re.sub("Game \d+: ", "", input_str)

        sets = res.split("; ")

        return [
            {
                x.split(" ")[1]: int(x.split(" ")[0])
                for x in one_set.split(", ")
            } for one_set in sets
        ]


    def part_one(self, raw_data: str):
        l_r, l_g, l_b = 12, 13, 14

        valid_games = []

        for game_idx, game in enumerate(raw_data.split("\n")):
            game_valid = True
            for game_set in self.row_to_tuple(game):
                if (game_set.get('red', 0) > l_r
                        or game_set.get('green', 0) > l_g
                        or game_set.get('blue', 0) > l_b):
                    game_valid = False
                    break
            if game_valid:
                valid_games.append(game_idx + 1)

        return str(sum(valid_games))


    def part_two(self, raw_data: str):
        game_powers = []

        for game in raw_data.split("\n"):
            r_min, g_min, b_min = 0, 0, 0
            for game_set in self.row_to_tuple(game):
                r_min = max(game_set.get('red', 0), r_min)
                g_min = max(game_set.get('green', 0), g_min)
                b_min = max(game_set.get('blue', 0), b_min)
            game_powers.append(r_min * g_min * b_min)

        return str(sum(game_powers))
    

if __name__ == '__main__':
    Day02().run()