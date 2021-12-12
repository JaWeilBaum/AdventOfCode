use itertools::{Itertools};
use std::fmt;

struct Node {
    identifier: String,
    connections: Vec<String>,
    multiple_visits_possible: bool
}

struct Edge {
    identifier: [String; 2]
}

impl fmt::Debug for Node {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Node")
            .field("identifier", &self.identifier)
            .field("connections", &self.connections)
            .field("multiple_visits_possible", &self.multiple_visits_possible)
            .finish()
    }
}

impl fmt::Debug for Edge {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Edge")
            .field("identifier", &self.identifier)
            .finish()
    }
}

fn is_capital(input: String) -> bool {
    input.to_uppercase() == input
}

fn get_all_connections(edges: &Vec<Edge>, identifier: String) -> Vec<String> {
    edges
        .into_iter()
        .filter(|x| x.identifier.iter().any(|x| *x == identifier))
        .flat_map(|x| (*x).identifier.to_vec())
        .filter(|x| *x != identifier)
        .collect_vec()
}

fn set_up_graph(content: String) -> Vec<Node> {
    let edges = content
        .split("\n")
        .collect_vec();

    let all_nodes = edges
        .iter()
        .flat_map(|&x| x.split("-").collect_vec())
        .collect_vec();

    let all_edges = edges
        .iter()
        .map(|x| x.split("-").map(|x| String::from(x)).collect_vec())
        .map(|x| Edge{identifier: [x[0].clone(), x[1].clone()]})
        .collect_vec();

    let distinct_nodes = all_nodes
        .into_iter()
        .unique()
        .collect_vec();

    let nodes: Vec<Node> = distinct_nodes
        .iter()
        .map(|&x| String::from(x))
        .map(|x| Node{
            identifier: x.clone(),
            connections: get_all_connections(&all_edges, x.clone()),
            multiple_visits_possible: is_capital(x.clone())
        })
        .collect_vec();

    return nodes
}

fn get_node(nodes: &Vec<Node>, name: String) -> &Node {
    nodes.iter().find(|x| x.identifier == name).unwrap()
}

fn open_closed_paths(paths: Vec<Vec<String>>) -> (Vec<Vec<String>>, Vec<Vec<String>>) {
    let open_paths = paths
        .iter()
        .filter(|x| x.last().unwrap() != "end" && x.last().unwrap() != "error")
        .map(|x| x.clone())
        .collect_vec();
    let closed_paths = paths
        .iter()
        .filter(|x| x.last().unwrap() == "end" || x.last().unwrap() == "error")
        .map(|x| x.clone())
        .collect_vec();
    return (open_paths, closed_paths);
}

fn algo(nodes: &Vec<Node>, num_visit_small_cave: u8) {
    let mut paths : Vec<Vec<String>> = vec![vec![String::from("start")]];
    let mut round_counter = 0;
    while true {
        round_counter += 1;
        println!("Round: {}", round_counter);
        let open_closed_paths_r = open_closed_paths(paths.clone());
        let open_paths = open_closed_paths_r.0;
        let closed_paths = open_closed_paths_r.1;

        if open_paths.len() == 0 {
            break
        }

        let mut new_paths: Vec<Vec<String>> = vec![];

        for path in open_paths.iter() {
            let last_element_in_path = path.last().unwrap().clone();
            let neighbours = get_node(&nodes, last_element_in_path).connections.clone()
                .iter()
                .filter(|&x| x != "start")
                .map(|x| x.clone())
                .collect_vec();

            for neighbour in neighbours {
                let mut new_path : Vec<String> = path.clone();
                let small_caves = path
                    .iter()
                    .filter(|&x| x.to_lowercase() == x.clone())
                    .map(|x| x.clone())
                    .collect_vec();

                let mut small_cave_visited_n_times = false;
                for small_cave in small_caves {
                    small_cave_visited_n_times |= path.iter().filter(|&x| x.clone() == small_cave).collect_vec().len() >= num_visit_small_cave as usize;
                }

                if path.contains(&neighbour) && small_cave_visited_n_times && neighbour.to_lowercase() == neighbour {
                    new_path.push(String::from("error"))
                } else {
                    new_path.push(String::from(neighbour))
                }
                new_paths.push(new_path)
            }
        }
        paths = closed_paths;
        paths.append(&mut new_paths)
    }

    let result = paths
        .iter()
        .filter(|x| x.last().unwrap() == "end")
        .collect_vec();

    println!("Done: {}", result.len())
}

pub fn run_01(content: String) {
    let nodes = set_up_graph(content);
    algo(&nodes, 1)
}

pub fn run_02(content: String) {
    let nodes = set_up_graph(content);
    algo(&nodes, 2)
}