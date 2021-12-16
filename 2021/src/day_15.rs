use itertools::{Itertools, all};
use std::cmp::min;
use std::os::unix::raw::time_t;

struct GPath {
    visited: Vec<(usize, usize)>,
    current_cost: u64
}

fn position_visited(path: &GPath, position: (usize, usize)) -> bool {
    path.visited.contains(&position)
}

fn get_next_paths(current_path: &GPath, field: &Vec<Vec<u64>>) -> Vec<GPath> {
    let current_position = current_path.visited.last().unwrap();
    let mut new_paths : Vec<GPath> = vec![];

    if current_position.0 < field.len() - 1 && !position_visited(&current_path, (current_position.0 + 1, current_position.1)) {
        let mut c = GPath{visited: current_path.visited.clone(), current_cost: current_path.current_cost};
        c.visited.push((current_position.0 + 1, current_position.1));
        c.current_cost += field[current_position.0 + 1][current_position.1];
        new_paths.push(c);
    }
    if current_position.0 > 0 && !position_visited(&current_path, (current_position.0 - 1, current_position.1)) {
        let mut c = GPath{visited: current_path.visited.clone(), current_cost: current_path.current_cost};
        c.visited.push((current_position.0 - 1, current_position.1));
        c.current_cost += field[current_position.0 - 1][current_position.1];
        new_paths.push(c);
    }
    if current_position.1 < field[0].len() - 1 && !position_visited(&current_path, (current_position.0, current_position.1 + 1)) {
        let mut c = GPath{visited: current_path.visited.clone(), current_cost: current_path.current_cost};
        c.visited.push((current_position.0, current_position.1 + 1));
        c.current_cost += field[current_position.0][current_position.1 + 1];
        new_paths.push(c);
    }
    if current_position.1 > 0 && !position_visited(&current_path, (current_position.0, current_position.1 - 1)) {
        let mut c = GPath{visited: current_path.visited.clone(), current_cost: current_path.current_cost};
        c.visited.push((current_position.0, current_position.1 - 1));
        c.current_cost += field[current_position.0][current_position.1 - 1];
        new_paths.push(c);
    }
    return new_paths
}

fn distance_to(from: &(usize, usize), to: &(usize, usize)) -> i64 {
    (from.0 as i64 - to.0 as i64).abs() as i64 + (from.1 as i64 - to.1 as i64).abs() as i64
}

pub fn run_01_rip(content: String) {
    let field = content
        .split("\n")
        .map(|x| x.chars().map(|x| x.to_digit(10).unwrap() as u64).collect_vec())
        .collect_vec();

    let source: (usize, usize) = (0, 0);
    let target: (usize, usize) = (field.len() - 1, field[0].len() - 1);
    println!("Source: {:?} Target: {:?}", source, target);
    let mut all_paths : Vec<GPath> = vec![GPath{visited: vec![source.clone()], current_cost: 0}];

    let mut counter = 0;
    while true {
        if counter % 10000 == 0 {
            println!("Round: {} num_paths: {} distance: {}", counter, all_paths.len(), distance_to(all_paths.last().unwrap().visited.last().unwrap(), &target));
        }
        counter += 1;
        let current_path = all_paths.pop().unwrap();
        let mut new_paths = get_next_paths(&current_path, &field);
        let paths_to_target = new_paths.iter().filter(|x| *x.visited.last().unwrap() == target).collect_vec();
        if paths_to_target.len() > 0 {
            println!("Found path: {:?}", paths_to_target.last().unwrap().visited);
            all_paths.push(GPath{visited: paths_to_target.last().unwrap().visited.clone(), current_cost: paths_to_target.last().unwrap().current_cost});
            break
        }
        all_paths.append(&mut new_paths);
        /*for path in all_paths.iter() {
            println!("{} {:?}", path.current_cost, path.visited);
        }*/
        all_paths.sort_by_key(|x| x.current_cost as i64/* - x.visited.len() as i64*/);
        if all_paths.len() > 5000 {
            for idx in 5000 - 1..all_paths.len() - 1 {
                all_paths.remove(idx);
            }
        }
        all_paths.reverse();
    }

    /*for path in all_paths.iter() {
        println!("{} {:?}", path.current_cost, path.visited);
    }*/

    //all_paths.sort_by_key(|x| x.current_cost * x.visited.len() as u64);
    //all_paths.reverse();
    let mut low_cost_path = all_paths.last().unwrap();

    println!();
    println!("{} {:?}", low_cost_path.current_cost, low_cost_path.visited);

    for y in 0..field.len() {
        for x in 0..field[y].len() {
            if low_cost_path.visited.contains(&(y, x)) {
                print!("#")
            } else {
                print!("{}", field[y][x])
            }
        }
        println!()
    }
}

struct Point {
    y: usize,
    x: usize,
    cost: u64
}

fn point_visited(points: &Vec<Point>, position: (usize, usize)) -> bool {
    points.iter().filter(|x| x.y == position.0 && x.x == position.1).collect_vec().len() > 0
}

fn point_lower(value: u64, points: &Vec<Point>, position: (usize, usize)) -> bool {
    points.iter().filter(|x| x.y == position.0 && x.x == position.1 && x.cost > value).collect_vec().len() > 0
}

fn get_next_points(current_point: &Point, visited_points: &Vec<Point>, field: &Vec<Vec<u64>>) -> Vec<Point> {
    let mut new_points : Vec<Point> = vec![];

    if current_point.y < field.len() - 1 && (!point_visited(&visited_points, (current_point.y + 1, current_point.x)) ||
        point_lower(current_point.cost + current_point.cost + field[current_point.y + 1][current_point.x], &visited_points, (current_point.y + 1, current_point.x))) {
        new_points.push(Point{x: current_point.x, y: current_point.y + 1, cost: current_point.cost + field[current_point.y + 1][current_point.x]});
    }
    if current_point.y > 0 && (!point_visited(&visited_points, (current_point.y - 1, current_point.x)) ||
        point_lower(current_point.cost + current_point.cost + field[current_point.y - 1][current_point.x], &visited_points, (current_point.y - 1, current_point.x))) {
        new_points.push(Point{x: current_point.x, y: current_point.y - 1, cost: current_point.cost + field[current_point.y - 1][current_point.x]});
    }
    if current_point.x < field[0].len() - 1 && (!point_visited(&visited_points, (current_point.y, current_point.x + 1)) ||
        point_lower(current_point.cost + current_point.cost + field[current_point.y][current_point.x + 1], &visited_points, (current_point.y, current_point.x + 1))) {
        new_points.push(Point{x: current_point.x + 1, y: current_point.y, cost: current_point.cost + field[current_point.y][current_point.x + 1]});
    }
    if current_point.x > 0 && (!point_visited(&visited_points, (current_point.y, current_point.x - 1)) ||
        point_lower(current_point.cost + current_point.cost + field[current_point.y][current_point.x - 1], &visited_points, (current_point.y, current_point.x - 1))) {
        new_points.push(Point{x: current_point.x - 1, y: current_point.y, cost: current_point.cost + field[current_point.y][current_point.x - 1]});
    }
    return new_points
}

pub fn run_01(content: String) {
    let field = content
        .split("\n")
        .map(|x| x.chars().map(|x| x.to_digit(10).unwrap() as u64).collect_vec())
        .collect_vec();

    let source = Point{y: 0, x: 0, cost: 0};
    let target: (usize, usize) = (field.len() - 1, field[0].len() - 1);

    let mut next_points: Vec<Point> = vec![source];
    let mut visited_points: Vec<Point> = vec![];

    let mut round = 0;
    while true {
        if round % 1000 == 0 {
            let next_point = next_points.iter().last().unwrap();
            println!("Round: {} num_next_points: {} distance: {}", round, next_points.len(), distance_to(&(next_point.y, next_point.x), &target));
        }
        round += 1;
        let mut current_point = next_points.pop().unwrap();
        let mut new_points = get_next_points(&current_point, &visited_points, &field);

        let solution_point = new_points.iter().filter(|x| x.y == target.0 && x.x == target.1).collect_vec();

        if solution_point.len() > 0 {
            let p = solution_point.last().unwrap();
            println!("Solution found!");
            println!("Point: {} y: {} x: {}", p.cost, p.y, p.x);
            break
        }

        for new_point in new_points {
            if !point_visited(&next_points, (new_point.y, new_point.x)) {
                next_points.push(new_point);
            }
        }
        // next_points.append(&mut new_points);
        visited_points.push(current_point);
        next_points.sort_by_cached_key(|x| x.cost);

        next_points.reverse();
    }

    /*for p in visited_points.iter() {
        println!("{} y: {} x: {}", p.cost, p.y, p.x);
    }*/

    for y in 0..field.len() {
        for x in 0..field[y].len() {
            print!("{}", field[y][x])
        }
        println!()
    }
}

fn extend_row(row: &Vec<u64>, times: u8) -> Vec<u64> {
    let mut return_row = vec![];
    let mut last_row = row.clone();
    for _ in 0..times {
        last_row = last_row.iter().map(|x| (x % 9) + 1).collect_vec();
        return_row.append(&mut last_row.clone())
    }
    return_row
}

fn extend_column(columns: &Vec<Vec<u64>>, times: u8) -> Vec<Vec<u64>> {
    let mut return_column = vec![];
    let mut current_columns = columns.clone();

    for _ in 0..times {
        for index in 0..current_columns.len() {
            current_columns[index] = extend_row(&current_columns[index], 1);
        }
        return_column.append(&mut current_columns.clone())
    }
    return_column
}

pub fn run_02(content: String) {
    let mut field = content
        .split("\n")
        .map(|x| x.chars().map(|x| x.to_digit(10).unwrap() as u64).collect_vec())
        .collect_vec();

    let mut extended_columns = extend_column(&field, 4);

    field.append(&mut extended_columns);

    for row_index in 0..field.len() {
        let current_row = field[row_index].clone();
        field[row_index].append(&mut extend_row(&current_row, 4));
        for e in field[row_index].iter() {
            print!("{}", e);
        }
        println!();
    }

    let source = Point{y: 0, x: 0, cost: 0};
    let target: (usize, usize) = (field.len() - 1, field[0].len() - 1);

    let mut next_points: Vec<Point> = vec![source];
    let mut visited_points: Vec<Point> = vec![];

    let mut round = 0;
    loop {
        if round % 1000 == 0 {
            let next_point = next_points.iter().last().unwrap();
            println!("Round: {} num_next_points: {} distance: {}", round, next_points.len(), distance_to(&(next_point.y, next_point.x), &target));
        }
        round += 1;
        let mut current_point = next_points.pop().unwrap();
        let mut new_points = get_next_points(&current_point, &visited_points, &field);

        let solution_point = new_points.iter().filter(|x| x.y == target.0 && x.x == target.1).collect_vec();

        if solution_point.len() > 0 {
            let p = solution_point.last().unwrap();
            println!("Solution found!");
            println!("Point: {} y: {} x: {}", p.cost, p.y, p.x);
            break
        }

        for new_point in new_points {
            if !point_visited(&next_points, (new_point.y, new_point.x)) {
                next_points.push(new_point);
            }
        }
        // next_points.append(&mut new_points);
        visited_points.push(current_point);
        next_points.sort_by_cached_key(|x| x.cost);

        next_points.reverse();
    }
}