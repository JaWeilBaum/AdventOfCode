use itertools::Itertools;

pub fn run_01(content: String) -> i32 {
    let mut fishes = content
        .split(",")
        .map(|x| x.parse::<u8>().unwrap())
        .collect_vec();

    // println!("Initial state: {:?}", fishes);
    let mut num_fish_before = fishes.len();
    for day in 0..80 {
        // println!("Before day {}: {:?}", day + 1, fishes);
        let num_new_fish = fishes.iter().filter(|&&x| x == 0).collect_vec().len();
        fishes = fishes.iter().map(|&x| {
            return if x == 0 {
                6
            } else {
                x - 1
            }
        }).collect_vec();

        for _ in 0..num_new_fish {
            fishes.push(8)
        }
        // println!("Day {} diff: +{}", day + 1, fishes.len() - num_fish_before);
        num_fish_before = fishes.len();
        // println!("After day {}: {:?} new_fish {}", day + 1, fishes, num_new_fish);
    }
    return fishes.len() as i32;
}

pub fn run_02(content: String) -> u128 {
    let mut fishes = content
        .split(",")
        .map(|x| x.parse::<u8>().unwrap())
        .collect_vec();

    // println!("Initial state: {:?}", fishes);
    let num_fish = fishes.len();

    let mut updates: [u128;9] = [0, 0, 0, 0, 0, 0, 0, 0, 0];

    for fish in fishes {
        updates[fish as usize] += 1;
    }

    // println!("Updates: {:?}", updates);

    for day in 0..256 {
        let recreated_fish = updates[0];
        updates[0] = updates[1];
        updates[1] = updates[2];
        updates[2] = updates[3];
        updates[3] = updates[4];
        updates[4] = updates[5];
        updates[5] = updates[6];
        updates[6] = updates[7] + recreated_fish;
        updates[7] = updates[8];
        updates[8] = recreated_fish;
        // println!("Day {} updates: {:?}", day + 1, updates);
        // println!("After day {}: {:?} new_fish {}", day + 1, fishes, num_new_fish);
    }
    return updates.into_iter().sum();
}