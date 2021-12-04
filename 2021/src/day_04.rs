use itertools::Itertools;

pub fn run_01(content: String) {
    let lines = content
        .split("\n")
        .collect::<Vec<&str>>();

    let numbers = lines[0]
        .split(",")
        .map(|x| i32::from_str_radix(x, 10).unwrap())
        .collect_vec();

    println!("{:?}", numbers);

    let mut current_field: Vec<Vec<i32>>= vec![];

    let mut fields: Vec<Vec<Vec<i32>>> = vec![];

    for index in 2..lines.len() {
        let current_line = lines[index];
        let mut field_line_numbers = current_line
            .split_ascii_whitespace()
            .map(|x| i32::from_str_radix(x, 10).unwrap())
            .collect_vec();
        if field_line_numbers.len() > 0 {
            current_field.push(field_line_numbers);
        } else {
            fields.push(current_field.clone());
            // println!("{:?}", current_field);
            current_field = vec![];
        }
    }

    for number in numbers {
        println!("Current number: {}", number);
        check_fields(&fields, number);
        return
    }

    /*for line in lines {
        println!("{}", line)
    }*/

}

fn check_fields(fields: &Vec<Vec<Vec<i32>>>, value: i32) {
    for field_index in 0..fields.len() {
        field = &fields[field_index];
        for row_index in 0..field.len() {
            row = field[row_index];
            for value_index in
        }
        println!("{:?}", field)
    }
}



pub fn run_02(content: String) {

}