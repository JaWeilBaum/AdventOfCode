mod day_03;
mod utils;

fn main() {
    let content = utils::get_file_str(String::from("./src/files/day03_input.txt"));

    let start_1 = std::time::Instant::now();

    day_03::run_01(content.clone());

    let end_1 = std::time::Instant::now();


    let start_2 = std::time::Instant::now();

    day_03::run_02(content.clone());

    let end_2 = std::time::Instant::now();

    println!("Task 1: {:?}", end_1 - start_1);
    println!("Task 2: {:?}", end_2 - start_2);
}
