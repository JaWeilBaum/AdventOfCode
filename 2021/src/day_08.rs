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

    let mut total_result = 0;

    for line in lines {

        let input_output = line
            .split(" | ")
            .map(|x| String::from(x))
            .collect::<Vec<String>>();

        let mut inputs = input_output[0]
            .split(" ")
            .map(|x| (String::from(x).chars().sorted().collect::<String>(), x.len()))
            .collect::<Vec<(String, usize)>>();

        let one = inputs.clone()
            .into_iter().filter(|x| x.1 == 2).last().unwrap().0;
        let seven = inputs.clone()
            .into_iter().filter(|x| x.1 == 3).last().unwrap().0;
        let four = inputs.clone()
            .into_iter().filter(|x| x.1 == 4).last().unwrap().0;
        let eight = inputs.clone()
            .into_iter().filter(|x| x.1 == 7).last().unwrap().0;

        let five_elements = inputs.clone()
            .into_iter().filter(|x| x.1 == 5).collect_vec();

        let six_elements = inputs.clone()
            .into_iter().filter(|x| x.1 == 6).collect_vec();

        let three = five_elements.clone()
            .into_iter().filter(|x| one.chars().into_iter().all(|y| x.0.contains(y))).last().unwrap().0;

        let nine = six_elements.clone()
            .into_iter().filter(|x| four.chars().into_iter().all(|y| x.0.contains(y))).last().unwrap().0;

        let zero = six_elements.clone()
            .into_iter().filter(|x| one.chars().into_iter().all(|y| x.0.contains(y)) && !four.chars().into_iter().all(|y| x.0.contains(y))).last().unwrap().0;

        let six = six_elements.clone()
            .into_iter().filter(|x| x.0 != nine && x.0 != zero).last().unwrap().0;

        let five = five_elements.clone()
            .into_iter().filter(|x| x.0 != three && nine.chars().into_iter().filter(|&y| x.0.contains(y)).count() == 5).last().unwrap().0;

        let two = five_elements.clone().
            into_iter().filter(|x| x.0 != three && x.0 != five).last().unwrap().0;

        println!("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}", zero, one, two, three, four, five, six, seven, eight, nine);

        let mapping = vec![
            (0, zero),
            (1, one),
            (2, two),
            (3, three),
            (4, four),
            (5, five),
            (6, six),
            (7, seven),
            (8, eight),
            (9, nine)
        ];

        let mut output = input_output[1]
            .split(" ")
            .map(|x| String::from(x).chars().sorted().collect::<String>())
            .map(|x| mapping.clone().into_iter().filter(|y| y.1 == x).last().unwrap().0)
            .collect_vec();


        let mut size = 1;
        let mut result = 0;

        for value in output.iter().rev() {
            result += value * size;
            size *= 10;
        }

        println!("Output: {}", result);
        total_result += result;
    }
    println!("Counter: {}", total_result);
}