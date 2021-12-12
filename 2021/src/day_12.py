import itertools

import networkx as nx


def run_01(content):
    edges = content.split("\n")

    all_nodes = []
    edge_tuples = []

    for edge in edges:
        edge_parts = edge.split("-")
        all_nodes += edge_parts
        edge_tuples.append((edge_parts[0], edge_parts[1]))

    distinct_nodes = set(all_nodes) - {"start", "end"}

    print(f"Distinct nodes: {distinct_nodes}")

    graph = nx.Graph()

    graph.add_nodes_from(distinct_nodes)
    graph.add_edges_from(edge_tuples)

    start_node = "start"

    paths = [[start_node]]
    new_paths = []
    while True:
        # print(f"Paths: {paths}")
        not_ended_paths, ended_paths = open_close_paths(paths)
        if len(not_ended_paths) == 0:
            break
        for _path in not_ended_paths:
            # print(f"Exploring path: {_path}")
            neighbours = set(graph.neighbors(_path[-1])) - {"start"}
            for neighbour in neighbours:
                if neighbour in _path and neighbour.lower() == neighbour:
                    new_path = _path + ["error"]
                else:
                    new_path = _path + [neighbour]
                # print(f"Appending new path {new_path}")
                new_paths.append(new_path)
        print(f"All new paths: {new_paths}")
        paths = ended_paths + new_paths.copy()
        new_paths = []

    counter = 0
    for _path in filter(lambda x: x[-1] == "end", paths):
        print(",".join(_path))
        counter += 1
    print(f"Done {counter}")


def open_close_paths(paths: list) -> (list, list):
    open_paths = list(filter(lambda x: not x[-1] in ["end", "error"], paths))
    closed_paths = list(filter(lambda x: x[-1] in ["end", "error"], paths))
    return open_paths, closed_paths


def run_02(content):
    edges = content.split("\n")

    all_nodes = []
    edge_tuples = []

    for edge in edges:
        edge_parts = edge.split("-")
        all_nodes += edge_parts
        edge_tuples.append((edge_parts[0], edge_parts[1]))

    distinct_nodes = set(all_nodes) - {"start", "end"}

    print(f"Distinct nodes: {distinct_nodes}")

    graph = nx.Graph()

    graph.add_nodes_from(distinct_nodes)
    graph.add_edges_from(edge_tuples)

    start_node = "start"

    paths = [[start_node]]
    new_paths = []
    round_counter = 0
    while True:
        round_counter += 1
        print(f"Round: {round_counter}")
        not_ended_paths, ended_paths = open_close_paths(paths)
        if len(not_ended_paths) == 0:
            break
        for _path in not_ended_paths:
            path: list[str]
            # print(f"Exploring path: {_path}")
            neighbours = list(set(graph.neighbors(_path[-1])) - {"start"})
            for neighbour in neighbours:
                all_small_caves = list(filter(lambda x: x.lower() == x, _path))
                one_visited_twice = False
                for c in all_small_caves:
                    one_visited_twice |= all_small_caves.count(c) == 2
                if one_visited_twice and neighbour in _path and neighbour.lower() == neighbour:
                    new_path = _path + ["error"]
                else:
                    new_path = _path + [neighbour]
                # print(f"Appending new path {new_path}")
                new_paths.append(new_path)
        # print(f"All new paths: {new_paths}")
        paths = ended_paths + new_paths.copy()
        new_paths = []

    print(f"Total paths: {len(paths)}")


if __name__ == '__main__':
    with open("files/day12_input.txt") as f:
        input_content = f.read()
    run_02(input_content)
