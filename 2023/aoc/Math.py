def mul(input_data: list[int]) -> int:
    return_value = input_data[0]
    for value in input_data[1:]:
        return_value = return_value * value
    return return_value