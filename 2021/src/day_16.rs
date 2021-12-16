use itertools::Itertools;

pub fn run_01(content: String) {
    let binary_input = content
        .chars()
        .map(|x| to_binary(x))
        .join("");

    let demo = "D2FE28".chars().map(|x| to_binary(x)).join("");
    let demo = "38006F45291200".chars().map(|x| to_binary(x)).join("");
    println!("{}", demo);
    parse(demo);
    parse_operator("00000000000110111101000101001010010001001000000000".to_owned())
    // parse_literal("101111111000101000".to_owned());
}

fn parse_literal(content: String) -> u32 {
    let mut number_bits: Vec<char> = vec![];
    for chunk in content.chars().collect_vec().chunks(5) {
        if chunk[0] == '0' && chunk.len() == 5 {
            println!("Last part")
        } else if chunk.len() != 5 {
            println!("Not complete, skipping!");
            continue
        }
        println!("{:?}", chunk[1..].to_vec());
        number_bits.append(&mut chunk[1..].to_vec());

    }
    let binary_number = String::from_iter(number_bits.iter());
    println!("{}", binary_number);
    println!("{}", u64::from_str_radix(&binary_number, 2).unwrap());

    return 0
}

fn parse_operator(content: String) {
    let number_bit = &content.chars().collect_vec()[0];
    let num_of_bits_packets = if *number_bit == '0' { 15 } else { 11 } as usize;
    let packets_bits = &content.chars().collect_vec()[1..num_of_bits_packets + 1];
    println!("{:?}", packets_bits);
    let num_packets = binary_string_to_value(String::from_iter(packets_bits.iter()));
    println!("Num packets: {}", num_packets)
}

fn binary_string_to_value(binary_string: String) -> u64 {
    u64::from_str_radix(&binary_string, 2).unwrap()
}

fn parse(packet: String) {
    let packet_version = u8::from_str_radix(&String::from_iter(packet.chars().collect_vec()[0..3].iter()), 2).unwrap();
    let packet_type_id = u8::from_str_radix(&String::from_iter(packet.chars().collect_vec()[3..6].iter()), 2).unwrap();
    println!("Version: {:?} Type ID: {:?}", packet_version, packet_type_id)
}

fn to_binary(c: char) -> String {
    return match c {
        '0' => "0000",
        '1' => "0001",
        '2' => "0010",
        '3' => "0011",
        '4' => "0100",
        '5' => "0101",
        '6' => "0110",
        '7' => "0111",
        '8' => "1000",
        '9' => "1001",
        'A' => "1010",
        'B' => "1011",
        'C' => "1100",
        'D' => "1101",
        'E' => "1110",
        'F' => "1111",
        _ => "",
    }.to_owned()
}