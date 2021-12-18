import json
import math


class Element:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

    def __str__(self):
        return "".join([" " for _ in range(self.depth - 1)]) + str(self.value)


def explode(element_list: list[Element]) -> bool:
    elements_to_explode = list(filter(lambda x: x[1].depth > 4, enumerate(element_list)))

    num_chunks = min(1, int(len(elements_to_explode) / 2))
    num_index_popped = 0

    for chunk in range(num_chunks):
        left_idx, left_element = elements_to_explode[chunk*2]
        right_idx, right_element = elements_to_explode[(chunk*2) + 1]

        if left_idx == 0:
            print("No explode since first element")
            element_list[right_idx + 1].value += right_element.value
            element_list.pop(left_idx)
            num_index_popped += 1
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1
            element_list.insert(0, Element(value=0, depth=element_list[right_idx].depth + 1))
            num_index_popped -= 1
        elif right_idx == len(element_list) - 1:
            print("No explode since last element")
            element_list[left_idx - 1].value += left_element.value
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1
            element_list.append(Element(value=0, depth=element_list[left_idx - num_index_popped].depth + 1))
            num_index_popped += 1
        else:
            element_list[right_idx + 1].value += right_element.value
            element_list[left_idx - 1].value += left_element.value
            element_list.pop(left_idx - num_index_popped)
            num_index_popped += 1
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1

            if element_list[left_idx - 1].depth == left_element.depth - 1:
                element_list.insert(left_idx, Element(value=0, depth=element_list[left_idx - 1].depth))
            else:
                element_list.insert(left_idx, Element(value=0, depth=element_list[left_idx].depth))


    return num_chunks != 0


def element_list_to_str(element_list: list[Element]) -> str:
    current_depth = element_list[0].depth
    return_str = "".join(["[" for _ in range(current_depth)])
    num_same_level = 0
    for index, e in enumerate(element_list):
        if current_depth < e.depth:
            return_str += "".join(["[" for _ in range(e.depth - current_depth)])
            num_same_level = 0
        elif current_depth > e.depth:
            return_str += "".join(["]" for _ in range(current_depth - e.depth)])
            num_same_level = 0
        else:
            num_same_level += 1

        if return_str[-1] in "]":
            return_str += ","

        return_str += str(e.value)

        if return_str[-1] in "0123456789":
            return_str += ","

        current_depth = e.depth
        if num_same_level == 2:
            return_str += "],["
            num_same_level = 0
    return_str += "]"

    return_str = return_str.replace(",]", "]")
    # return_str = return_str.replace(",[", "[")
   #  return_str = return_str.replace("[,", "[")

    return return_str


def get_data() -> str:
    # return "[[2,[3,[4,[9,8]]]]],1]"
    # return "[[[[[9,8],1],2],3],4]"
    # return "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]"
    # return "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
    # return "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
    return "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    # return "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
    # return "[[6,[5,[4,[3,2]]]],1]"
    # return "[[6,[5,[[3,2],4]]],1]"
    # [[6,[8,[0,6]]],1]


def parse(input_str: str) -> list[Element]:
    element_list = []
    depth = 0

    for index, char in enumerate(input_str):
        # print(f"Idx: {index} = {char} Depth: {depth}")
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char in "0123456789":
            element_list.append(Element(value=int(char), depth=depth))

    return element_list


def step(input_list: list[Element]) -> bool:
    explode_bool = explode(input_list)
    split_bool = split(input_list)
    return explode_bool or split_bool


def split(input_list: list[Element]) -> bool:
    for index, e in enumerate(input_list):

        if e.value >= 10:
            new_left = Element(value=math.floor(e.value / 2), depth=e.depth + 1)
            new_right = Element(value=math.ceil(e.value / 2), depth=e.depth + 1)
            input_list.pop(index)
            input_list.insert(index, new_left)
            input_list.insert(index + 1, new_right)
            return True
    return False


def show_list(input_list: list[Element]):
    for e in input_list:
        print(e)


def main():
    one_line = get_data()
    element_list = parse(one_line)

    while step(element_list):
        print()
        show_list(element_list)



if __name__ == '__main__':
    main()