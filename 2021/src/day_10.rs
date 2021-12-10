use itertools::{Itertools, enumerate};

pub fn run_01(content: String) {
    let lines = content
        .split("\n")
        .map(|x| String::from(x).chars().collect_vec())
        .collect_vec();

    let mut total_score = 0;

    for line in lines {
        let mut error_occ = false;
        let mut closing_list: Vec<char> = vec![];
        for (index, c) in enumerate(line) {
            if is_opening_char(&c) {
                closing_list.push( get_closing_char(&c));
            } else if *closing_list.last().unwrap() == c {
                let test = closing_list.pop().unwrap();
            } else {
                total_score += illegal_char_cost(&c);
                error_occ = true;
                break
            }
        }
        if !error_occ {
            println!("No Error")
        }
    }
    println!("Total score: {}", total_score);
}

fn illegal_char_cost(c: &char) -> i32 {
    return if *c == ')' {
        3
    } else if *c == ']' {
        57
    } else if *c == '}' {
        1197
    } else if *c == '>' {
        25137
    } else {
        -100000
    }
}

fn is_opening_char(c: &char) -> bool {
    return *c == '(' || *c == '{' || *c == '[' || *c == '<'
}

fn get_closing_char(c: &char) -> char {
    return if *c == '(' {
        ')'
    } else if *c == '{' {
        '}'
    } else if *c == '[' {
        ']'
    } else if *c == '<' {
        '>'
    } else {
        ' '
    }
}

fn completion_char_cost(c: &char) -> u128 {
    return if *c == ')' {
        1
    } else if *c == ']' {
        2
    } else if *c == '}' {
        3
    } else if *c == '>' {
        4
    } else {
        0
    }
}

fn calculate_score(closing_seq: &Vec<char>) -> u128 {
    let mut score: u128 = 0;
    for c in closing_seq {
        score *= 5;
        score += completion_char_cost(c);
    }
    return score
}

/// Basically the solution of before, since it already contains
/// the closing list which is required to determine the score
pub fn run_02(content: String) {
    let lines = content
        .split("\n")
        .map(|x| String::from(x).chars().collect_vec())
        .collect_vec();

    let mut completion_costs: Vec<u128> = vec![];

    for line in lines {
        let mut error_occ = false;
        let mut closing_list: Vec<char> = vec![];
        for (index, c) in enumerate(line) {
            if is_opening_char(&c) {
                closing_list.push( get_closing_char(&c));
            } else if *closing_list.last().unwrap() == c {
                let test = closing_list.pop().unwrap();
            } else {
                error_occ = true;
                break
            }
        }
        if !error_occ {
            completion_costs.push(calculate_score(&closing_list.into_iter().rev().collect_vec()));
        }
    }
    let half_point = (completion_costs.len() / 2) as usize;
    completion_costs.sort();

    println!("Score: {}", completion_costs[half_point]);
}