use itertools::Itertools;

pub fn run_01(content: String) {
    let lines = content
        .split("\n")
        .map(|x| String::from(x))
        .collect::<Vec<String>>();

    let mut counter = 0;

    for line in lines {
        let num_relevant_parts = line
            .split(" | ").last().unwrap()
            .split(" ")
            .map(|x| String::from(x))
            .map(|x| x.len())
            .map(|x| (x == 2 || x == 3 || x == 4 || x == 7) as u8)
            .sum::<u8>();
        println!("{}", num_relevant_parts);
        counter += num_relevant_parts as i32;
    }
    println!("Counter: {}", counter)
}


struct Digit {
    top_center: char,
    top_left: char,
    top_right: char,
    center: char,
    bottom_left: char,
    bottom_right: char,
    bottom_center: char,
}


pub fn run_02(content: String) {
    let lines = content
        .split("\n")
        .map(|x| String::from(x))
        .collect::<Vec<String>>();

    for line in lines {

        let input_output = line
            .split(" | ")
            .map(|x| String::from(x))
            .collect::<Vec<String>>();

        let mut inputs = input_output[0]
            .split(" ")
            .map(|x| (String::from(x), x.len()))
            .collect::<Vec<(String, usize)>>();

        inputs.sort_by_key(|x| x.1);

        /**
         1
        0 2
         3
        4 6
         5
        **/

        let mut digit = [' ',' ',' ',' ',' ',' ',' '];
        let mut chars_done: Vec<char> = vec![];

        let two = inputs
            .iter().filter(|x| x.1 == 2).last().unwrap().0.chars().collect::<Vec<char>>();

        digit[2] = two[0];
        digit[6] = two[1];

        chars_done.push(two[0]);
        chars_done.push(two[1]);

        let three = inputs
            .iter().filter(|x| x.1 == 3).last().unwrap().0.chars().collect::<Vec<char>>()
            .into_iter().filter(|x| !chars_done.contains(x)).collect::<Vec<char>>();

        digit[1] = three[0];

        chars_done.push(three[0]);

        let four = inputs
            .iter().filter(|x| x.1 == 4).last().unwrap().0.chars().collect::<Vec<char>>()
            .into_iter().filter(|x| !chars_done.contains(x)).collect::<Vec<char>>();
        println!("{:?}", four);

        println!("{:?}", digit);


        


        println!("[In]: {} [Out]: {}", input_output[0], input_output[1]);
        println!("{:?}", inputs);
    }
    // println!("Counter: {}", counter)
}