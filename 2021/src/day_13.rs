use itertools::{Itertools, enumerate};

pub fn run_01(content: String) {
    let parts = content.split("\n\n").collect_vec();

    let coordinates: Vec<(usize, usize)> = parts[0]
        .split("\n")
        .map(|x| x.split(",").map(|x| x.parse::<usize>().unwrap()).collect_tuple().unwrap())
        .collect_vec();

    let raw_fold_instructions = parts[1]
        .split("\n")
        .map(|x| x.replace("fold along ", ""))
        .collect_vec();

    let fold_instructions = raw_fold_instructions
        .iter()
        .map(|x| x.split("=").collect_vec())
        .map(|x| (String::from(x[0]), x[1].parse::<usize>().unwrap()))
        .collect_vec();


    let max_x = coordinates.iter().map(|x| x.0).max().unwrap();
    let mut max_y = coordinates.iter().map(|x| x.1).max().unwrap();
    if (max_y + 1) % 2 == 0 {
        max_y += 1;
    }

    let mut field = vec![vec![false;max_x + 1];max_y + 1];

    coordinates
        .iter()
        .map(|x| field[x.1][x.0] = true)
        .collect_vec();

    let mut current_field = field;

    fold_instructions
        .iter()
        .map(|(axis, level)| current_field = fold(&current_field, &axis, &level))
        .collect_vec();

    /*for (axis, level) in fold_instructions {
        current_field = fold(&current_field, &axis, &level).clone();
        println!("Folding {} at {} Visible fields: {}", axis, level, count(&current_field));
    }*/
    print(&current_field);
}

fn print(field: &Vec<Vec<bool>>) {
    for row in field.iter() {
        for element in row.iter() {
            if *element {
                print!("#")
            } else {
                print!(" ")
            }
        }
        println!()
    }
}

fn flip(field: &Vec<Vec<bool>>, axis: &String) -> Vec<Vec<bool>> {
    return if *axis == "y" {
        field
            .clone()
            .into_iter()
            .rev()
            .collect_vec()
    } else {
        field
            .clone()
            .into_iter()
            .map(|x| x
                .into_iter()
                .rev()
                .collect_vec())
            .collect_vec()
    }
}

fn merge(half_0: &Vec<Vec<bool>>, half_1: &Vec<Vec<bool>>) -> Vec<Vec<bool>> {
    half_0
        .iter()
        .enumerate()
        .map(|(y, _)| half_0[y]
            .iter()
            .zip(half_1[y].iter())
            .map(|(x, y)| *x || *y)
            .collect_vec())
        .collect_vec()
}

fn split(field: &Vec<Vec<bool>>, axis: &String, level: &usize) -> (Vec<Vec<bool>>, Vec<Vec<bool>>) {
    return if *axis == String::from("y") {
        let halfs = field.split_at(*level);
        let half_0 = halfs.0.to_vec();
        let mut half_1 = halfs.1.to_vec();
        if field.len() % 2 != 0 {
            half_1.remove(0);
        }
        half_1 = flip(&half_1, axis);
        (half_0, half_1)
    } else {
        let half_0 = (0..field.len())
            .into_iter()
            .map(|y| (0..*level)
                .into_iter()
                .map(|x| field[y][x])
                .collect_vec())
            .collect_vec();

        let half_1 = (0..field.len())
            .into_iter()
            .map(|y| (0..*level)
                .into_iter()
                .map(|x| field[y][x + *level + 1])
                .collect_vec())
            .collect_vec();
        (half_0, flip(&half_1, axis))
    }

}

fn fold(field: &Vec<Vec<bool>>, axis: &String, level: &usize) -> Vec<Vec<bool>> {
    let halfs = split(field, axis, level);
    let result = merge(&halfs.0, &halfs.1);
    return result
}

fn count(field: &Vec<Vec<bool>>) -> u16 {
    field
        .iter()
        .map(|x| x.iter().map(|y| *y as u16).sum::<u16>())
        .sum::<u16>()
}

pub fn run_02(content: String) {

}