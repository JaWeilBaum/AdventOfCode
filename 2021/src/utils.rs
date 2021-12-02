use std::fs::File;
use std::io::prelude::*;

pub fn get_file_str(file_path: String) -> String {
    let mut file = File::open(file_path).expect("POOF");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("POOF");
    return content
}