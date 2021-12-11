use itertools::{Itertools, enumerate};
use std::fmt;

struct DumboOcto {
    value: u8,
    flashed: bool
}

impl fmt::Debug for DumboOcto {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("DumboOcto")
            .field("value", &self.value)
            .field("flashed", &self.flashed)
            .finish()
    }
}

impl Copy for DumboOcto { }

impl Clone for DumboOcto {
    fn clone(&self) -> Self {
        *self
    }
}

fn light_up_adjacent(field: &mut Vec<Vec<DumboOcto>>, coordinates: (i8, i8)) {
    if coordinates.0 < 0 || coordinates.1 < 0 {
        return
    }
    let y = coordinates.0 as usize;
    let x =  coordinates.1 as usize;
    if y >= field.len() {
        return
    }
    if x >= field[y].len() {
        return
    }
    field[y][x].value += 1 as u8;
}

fn simulation_step(field: &mut Vec<Vec<DumboOcto>>) -> u16 {
    for y in 0..field.len() {
        for x in 0..field[y].len() {
            field[y][x].value += 1;
        }
    }

    // print_board(field, false);

    let mut num_changes = 1;
    while num_changes != 0 {
        num_changes = 0;
        for y in 0..field.len() {
            for x in 0..field[y].len() {
                if field[y][x].value > 9 && !field[y][x].flashed {
                    field[y][x].flashed = true;
                    num_changes += 1;
                    light_up_adjacent(field, (y as i8 - 1, x as i8 - 1));
                    light_up_adjacent(field, (y as i8 + 1, x as i8 - 1));
                    light_up_adjacent(field, (y as i8 - 1, x as i8 + 1));
                    light_up_adjacent(field, (y as i8 + 1, x as i8 + 1));
                    light_up_adjacent(field, (y as i8, x as i8 - 1));
                    light_up_adjacent(field, (y as i8, x as i8 + 1));
                    light_up_adjacent(field, (y as i8 - 1, x as i8));
                    light_up_adjacent(field, (y as i8 + 1, x as i8));
                }
            }
        }
    }
    // print_board(field, true);
    // print_board(field, false);

    let mut num_flashes = 0;
    for y in 0..field.len() {
        for x in 0..field[y].len() {
            if field[y][x].flashed {
                field[y][x].value = 0;
                field[y][x].flashed = false;
                num_flashes += 1;
            }
        }
    }

    // print_board(field, false);

    return num_flashes;
}

fn print_board(field: &Vec<Vec<DumboOcto>>, flashed: bool) {
    if flashed {
        println!("Board: 'Flashed'")
    } else {
        println!("Board: 'Values'")
    }
    for y in 0..field.len() {
        for x in 0..field[y].len() {
            if flashed {
                print!("{}", field[y][x].flashed as u8)
            } else {
                if field[y][x].value < 10 {
                    print!("  {} ", field[y][x].value)
                } else {
                    print!(" {} ", field[y][x].value)
                }
            }
        }
        println!()
    }
    println!()
}

pub fn run_01(content: String) {
    let mut field = content
        .split('\n')
        .map(|x| x.chars().map(|y|DumboOcto{value: y.to_digit(10).unwrap() as u8, flashed: false}).collect_vec())
        .collect_vec();

    let mut total_flashes = 0;
    for round in 0..100 {
        let result = simulation_step(&mut field);
        println!("Round: {} Num flashes {}", round + 1, result);
        total_flashes += result;
    }
    println!("Total flashes: {}", total_flashes)
}

fn sum_field(field: &Vec<Vec<DumboOcto>>) -> u16 {
    field.iter().map(|x| x.iter().map(|&y| y.value as u16).sum::<u16>()).sum::<u16>()
}

pub fn run_02(content: String) {
    let mut field = content
        .split('\n')
        .map(|x| x.chars().map(|y|DumboOcto{value: y.to_digit(10).unwrap() as u8, flashed: false}).collect_vec())
        .collect_vec();


    for round in 0..500 {
        let result = simulation_step(&mut field);
        let field_sum_result = sum_field(&field);
        if field_sum_result == 0 {
            println!("Round: {} total field sum {}", round + 1, field_sum_result);
            break;
        }
    }
}
