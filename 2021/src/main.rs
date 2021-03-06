mod day_16;
mod utils;

fn main() {
    let content = utils::get_file_str(String::from("./src/files/day16_input.txt"));
    // let content =  String::from("16,1,2,0,4,2,7,1,2,14");

    let start_1 = std::time::Instant::now();

    day_16::run_01(content.clone());

    let end_1 = std::time::Instant::now();


    let start_2 = std::time::Instant::now();

    // day_15::run_02(content.clone());

    let end_2 = std::time::Instant::now();

    println!("Task 1: {:?}", end_1 - start_1);
    println!("Task 2: {:?}", end_2 - start_2);
}
