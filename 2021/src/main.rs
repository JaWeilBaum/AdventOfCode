mod day_01;

fn main() {
    let start_1 = std::time::Instant::now();
    day_01::run_01();
    let end_1 = std::time::Instant::now();
    let start_2 = std::time::Instant::now();
    day_01::run_02();
    let end_2 = std::time::Instant::now();
    println!("Task 1: {:?}", end_1 - start_1);
    println!("Task 2: {:?}", end_2 - start_2);
}
