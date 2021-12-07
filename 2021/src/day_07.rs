use itertools::{Itertools, min};

pub fn run_01(content: String) {
    let numbers = content
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect_vec();

    let mut min_distance = i32::MAX;

    for i in 0..=*numbers.iter().max().unwrap() {
        let distance = numbers.iter().map(|x| (i - *x).abs()).sum();
        if distance > min_distance {
            break;
        }
        min_distance = distance;
    }
    println!("Total fuel cost from {}", min_distance);
}

fn fuel_cons_02(distance: i32) -> i32 {
    (distance * (distance + 1)) / 2
}


pub fn run_02(content: String) {
    let numbers = content
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect_vec();

    let mut min_distance = i32::MAX;

    for i in 0..=*numbers.iter().max().unwrap() {
        let distance = numbers.iter().map(|x| fuel_cons_02((i - *x).abs())).sum();
        if distance > min_distance {
            break;
        }
        min_distance = distance;
    }
    println!("Total fuel cost from {}", min_distance);
}