use itertools::Itertools;

pub fn run_01(content: String) {
    let lines = content
        .split("\n")
        //.map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    let mut pos_horizontal = 0;
    let mut pos_vertical = 0;

    for line in lines {

        let (direction_str, distance_str): (&str, &str) = line.split_ascii_whitespace().collect_tuple().unwrap();

        let mut distance = distance_str.parse::<i32>().unwrap();

        let mut vertical = (direction_str == "up" || direction_str == "down") as i32 * distance;
        vertical -= 2 * vertical * (direction_str == "up") as i32;
        let horizontal = (direction_str == "forward") as i32 * distance;

        pos_horizontal += horizontal;
        pos_vertical += vertical;

        // println!("Direction: {}, Distance: {} - Vertical: {} Horizontal: {}", direction_str, distance, vertical, horizontal)
    }

    println!("Position H: {} V: {} Product: {}", pos_horizontal, pos_vertical, pos_horizontal * pos_vertical);
}

pub fn run_02(content: String) {
    let lines = content
        .split("\n")
        //.map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    let mut pos_horizontal = 0;
    let mut pos_vertical = 0;
    let mut pos_aim = 0;

    for line in lines {
        let (direction_str, distance_str): (&str, &str) = line.split_ascii_whitespace().collect_tuple().unwrap();

        let mut distance = distance_str.parse::<i32>().unwrap();

        let is_forward = (direction_str == "forward") as i32;

        let horizontal = is_forward * distance;
        let mut new_aim = (direction_str == "up" || direction_str == "down") as i32 * distance;
        new_aim += -2 * new_aim * (direction_str == "up") as i32;

        /* SLOW
        if direction_str == "forward" {
            pos_horizontal += horizontal;
            pos_vertical += horizontal * pos_aim;
        } else {
            pos_aim += new_aim;
        }
        */

        pos_horizontal += horizontal * is_forward;
        pos_vertical += (horizontal * pos_aim) * is_forward;
        pos_aim += (is_forward != 1) as i32 * new_aim;

        // println!("Direction: {}, Distance: {} | Pos_horizontal: {} Pos_vertical: {} cur_aim: {} - new_aim: {}", direction_str, distance, pos_horizontal, pos_vertical, pos_aim, new_aim)
    }

    println!("Position H: {} V: {} Product: {}", pos_horizontal, pos_vertical, pos_horizontal * pos_vertical);
}