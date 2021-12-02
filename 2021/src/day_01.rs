pub fn run_01(content: String) {
    let parts = content.split("\n");
    let mut previous_measurement: i32 = i32::MAX;
    let mut increased_counter = 0;

    for part in parts {
        // let mut changed_value = String::new();
        let measurement = part.parse::<i32>().unwrap_or(i32::MIN);

        if previous_measurement < measurement {
            increased_counter += 1;
            // changed_value = String::from("Increased");
        } else {
            // changed_value = String::from("Decreased");
        }

        // println!("{} ({})", part, changed_value);
        previous_measurement = measurement;
    }

    println!("Total increases: {}", increased_counter);
}

pub fn run_02(content: String) {
    let mut increased_counter = 0;

    let lines = content
        .split("\n")
        .map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    /*
    0  A   ==> a
    1  A B ==> ab_1
    2  A B ==> ab_2
    3    B ==> b

     */

    for index in 0..lines.len() - 3 {
        let (a, ab_1, ab_2, b) = (lines[index], lines[index + 1], lines[index + 2], lines[index + 3]);

        let left = a + ab_1 + ab_2;
        let right = ab_1 + ab_2 + b;

        increased_counter += (left < right) as i32;
        // println!("Index: {}", index);
        // println!("{} + {} + {} = {}", a, ab_1, ab_2, left);
        // println!("{} + {} + {} = {}", ab_1, ab_2, b, right);
        // println!("{}", (left < right) as i32)
    }

    println!("Total increases: {}", increased_counter)
}