from aoc import Day
import networkx as nx


class Day25(Day):

    def __init__(self):
        super().__init__(25)

    def part_one(self, raw_data: str) -> str:
        rows = raw_data.splitlines()

        connections = {}

        for row in rows:
            k, vs = row.split(":")
            for v in vs.split():
                if k not in connections:
                    connections[k] = {v}
                else:
                    connections[k].add(v)
                if v not in connections:
                    connections[v] = {k}
                else:
                    connections[v].add(k)

        G = nx.DiGraph()
        for k, vs in connections.items():
            for v in vs:
                G.add_edge(k, v, capacity=1)
                G.add_edge(v, k, capacity=1)

        for x in connections.keys():
            for y in connections.keys():
                if x != y:
                    cut_value, (g1, g2) = nx.minimum_cut(G, x, y)
                    if cut_value == 3:
                        return str(len(g1) * len(g2))

        pass

    def part_two(self, raw_data: str) -> str:
        pass


if __name__ == '__main__':
    Day25().run(False, True, False)