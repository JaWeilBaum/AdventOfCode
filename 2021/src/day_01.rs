use std::fs::File;
use std::io::prelude::*;

pub fn run() -> std::io::Result<()> {
    let mut file = File::open("./src/files/day01_0_input")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let parts = content.split("\n");
    let mut previous_measurement: i32 = i32::MAX;
    let mut increased_counter = 0;

    for part in parts {
        let mut changed_value = String::new();
        let measurement = part.parse::<i32>().unwrap_or(i32::MIN);

        if previous_measurement < measurement {
            increased_counter += 1;
            changed_value = String::from("Increased");
        } else {
            changed_value = String::from("Decreased");
        }

        println!("{} ({})", part, changed_value);
        previous_measurement = measurement;
    }

    println!("Total increases: {}", increased_counter);

    Ok(())
}