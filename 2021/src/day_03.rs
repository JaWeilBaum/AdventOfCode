use itertools::Itertools;

pub fn run_01(content: String) {
    let lines = content
        .split("\n")
        .collect::<Vec<_>>();

    let half = (lines.len() / 2) as u32;

    let mut cols = vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    for line in lines {
        let char_vector = line
            .chars()
            .map(|x| x.to_digit(f32::RADIX).unwrap())
            .collect::<Vec<u32>>();

        cols = cols.iter().zip(char_vector.iter()).map(|(b, v)| b + v).collect_vec();

        // println!("{:?} -> {:?}", char_vector, cols);
    }

    let gamma_vec = cols.iter().map(|&x| String::from(((x > half) as u32).to_string())).collect_vec();
    let epsilon_vec = cols.iter().map(|&x| String::from(((x < half) as u32).to_string())).collect_vec();

    let gamma_bin_str: String = gamma_vec.join("");
    let epsilon_bin_str: String = epsilon_vec.join("");

    let gamma = isize::from_str_radix(&gamma_bin_str, 2).unwrap();
    let epsilon = isize::from_str_radix(&epsilon_bin_str, 2).unwrap();

    println!("Gamma {} ({})", gamma, gamma_bin_str);
    println!("Epsilon {}, ({})", epsilon, epsilon_bin_str);
    println!("Product: {}", gamma * epsilon);
}

fn get_higher_occurrence(rows: Vec<Vec<u32>>, index: usize, tiebreaker: u32) -> u32 {
    let mut cols = vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    let length = rows.len() as u32;

    for row in rows {
        cols = cols.iter().zip(row.iter()).map(|(b, v)| b + v).collect_vec();
    }
    let value = cols[index];
    //println!("half: {} cols: {:?}", length as f32 / 2.0, cols);
    if value * 2 == length {
        //println!("TIEBREAKER");
        return tiebreaker;
    }
    return ((value * 2) > length) as u32;
}

fn filter_vector(current: Vec<Vec<u32>>, index: usize, keep_value: u32) -> Vec<Vec<u32>> {
    return current.into_iter().filter(|x| x[index] == keep_value).collect_vec()
}


pub fn run_02(content: String) {
    let lines = content
        .split("\n")
        .map(|s| s
            .chars()
            .map(|x| x.to_digit(f32::RADIX).unwrap()).collect_vec())
        .collect::<Vec<Vec<u32>>>();

    let mut current_lines = lines.clone();

    let mut oxygen:u32 = 0;

    for index in 0..12 {
        let higher_bit = get_higher_occurrence(current_lines.clone(), index as usize, 1);
        current_lines = filter_vector(current_lines, index as usize, higher_bit);
        // println!("keep: {} total_rows: {}", higher_bit, current_lines.len());
        if current_lines.len() == 1 {
            let oxygen_string = current_lines[0].iter().map(|&x| x.to_string()).join("");
            oxygen = u32::from_str_radix(&oxygen_string, 2).unwrap();
            println!("Oxygen: {}", oxygen);
            break;
        }
    }

    let mut co2: u32 = 0;

    current_lines = lines.clone();

    for index in 0..12 {
        let mut higher_bit = get_higher_occurrence(current_lines.clone(), index as usize, 0);
        if current_lines.len() != 2 {
            higher_bit = (higher_bit != 1) as u32;
        }
        current_lines = filter_vector(current_lines, index as usize, higher_bit);
        // println!("Index: {} most_bit: {} total_rows: {}", index, higher_bit, current_lines.len());
        if current_lines.len() == 1 {
            let co2_string = current_lines[0].iter().map(|&x| x.to_string()).join("");
            co2 = u32::from_str_radix(&co2_string, 2).unwrap();
            println!("CO2: {}", co2);
            break;
        }
    }

    println!("Product: {}", oxygen * co2);
}