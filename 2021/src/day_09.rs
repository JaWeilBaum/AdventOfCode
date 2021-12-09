use itertools::{Itertools, enumerate, rev};
use core::arch::x86_64::_mm256_undefined_pd;
use std::cmp::min;

pub fn run_01(content: String) {
    let numbers = content
        .split("\n")
        .map(|x| String::from(x).chars().map(|x| String::from(x).parse::<u8>().unwrap()).collect_vec())
        .collect_vec();

    let mut minimums = 0;

    /**
    012345
    1
    2
    3
    4
    5
    **/

    // let mut counter: Vec<Vec<i32>> = vec![vec![0;10];5];

    let mut risk_counter = 0;

    for y in 0..numbers.len() {
        for x in 0..numbers[y].len() {
            let mut lower_counter = 0;
            if y == 0 {
                lower_counter += 1;
                lower_counter += (numbers[y][x] < numbers[y + 1][x]) as i32;
            } else if y == numbers.len() - 1 {
                lower_counter += 1;
                lower_counter += (numbers[y][x] < numbers[y - 1][x]) as i32;
            } else {
                lower_counter += (numbers[y][x] < numbers[y + 1][x]) as i32;
                lower_counter += (numbers[y][x] < numbers[y - 1][x]) as i32;
            }
            if x == 0 {
                lower_counter += 1;
                lower_counter += (numbers[y][x] < numbers[y][x + 1]) as i32;
            } else if x == numbers[y].len() - 1 {
                lower_counter += 1;
                lower_counter += (numbers[y][x] < numbers[y][x - 1]) as i32;
            } else {
                lower_counter += (numbers[y][x] < numbers[y][x + 1]) as i32;
                lower_counter += (numbers[y][x] < numbers[y][x - 1]) as i32;
            }

            // counter[y][x] = lower_counter;
            risk_counter += (lower_counter == 4) as i32 * (numbers[y][x] + 1) as i32;
        }
    }

    /* for row in counter {
        println!("{:?}", row);
    }*/

    println!("Risklevel: {}", risk_counter);
}

fn get_next(zero_indices: &Vec<(usize, usize)>, current_index: (usize, usize)) -> Vec<(usize, usize)> {
    let mut return_vec: Vec<(usize, usize)> = vec![];
    if zero_indices.contains(&(current_index.0 + 1, current_index.1)) {
        return_vec.push((current_index.0 + 1, current_index.1))
    }
    if current_index.0 > 0 && zero_indices.contains(&(current_index.0 - 1, current_index.1)) {
        return_vec.push((current_index.0 - 1, current_index.1))
    }
    if zero_indices.contains(&(current_index.0, current_index.1 + 1)) {
        return_vec.push((current_index.0, current_index.1 + 1))
    }
    if current_index.1 > 0 && zero_indices.contains(&(current_index.0, current_index.1 - 1)) {
        return_vec.push((current_index.0, current_index.1 - 1))
    }
    return return_vec;
}

/// Not fast but efficient
///
pub fn run_02(content: String) {
    let numbers = content
        .split("\n")
        .map(|x| String::from(x)
            .chars()
            .map(|x| String::from(x).parse::<u8>().unwrap())
            .map(|x| return if x == 9 { return x } else { return 0}).collect_vec())
        .collect_vec();

    let mut zero_indices : Vec<(usize, usize)> = vec![];

    for (y, row) in enumerate(numbers) {
        for (x, number) in enumerate(row) {
            if number == 0 {
                zero_indices.push((y, x))
            }
            print!("{}", number);
        }
        println!();
    }


    let mut basin_size: Vec<i32> = vec![];
    println!("{:?}", zero_indices);

    while zero_indices.len() > 0 {
        let mut basin_indexes: Vec<(usize, usize)> = vec![];

        let current_index = zero_indices.pop().unwrap();

        basin_indexes.push(current_index);

        let mut len_before = 0;

        while len_before != basin_indexes.len() {
            len_before = basin_indexes.len();
            let mut new_indices: Vec<(usize, usize)> = vec![];
            for index_pair in &basin_indexes {
                let next_values = get_next(&zero_indices, *index_pair);
                for value in next_values {
                    if !basin_indexes.contains(&value) {
                        new_indices.push(value)
                    }
                }
            }
            for new_index in new_indices {
                if !basin_indexes.contains(&new_index) {
                    basin_indexes.push(new_index)
                }
            }
        }

        basin_size.push(basin_indexes.len() as i32);

        zero_indices = zero_indices.into_iter().filter(|x| !basin_indexes.contains(x)).collect_vec();
    }


    basin_size = basin_size.into_iter().sorted().rev().collect_vec();

    println!("Basi sizes: {:?}", basin_size);
    println!("Answer: {:?}", basin_size[0] * basin_size[1] * basin_size[2])
}