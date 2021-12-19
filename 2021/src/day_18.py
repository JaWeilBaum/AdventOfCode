import json
import math


class Element:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

    def __str__(self):
        return "".join([" " for _ in range(self.depth - 1)]) + str(self.value)


def explode_depth(element_list: list[Element]) -> (int, int):
    elements_to_explode = list(sorted(list(filter(lambda x: x[1].depth > 4, enumerate(element_list))), key=lambda x: x[0]))
    if len(elements_to_explode) == 0:
        return -1, -1
    return elements_to_explode[0][1].depth, elements_to_explode[0][0]


def explode(element_list: list[Element]) -> bool:
    elements_to_explode = list(sorted(list(filter(lambda x: x[1].depth > 4, enumerate(element_list))), key=lambda x: x[1].depth, reverse=True))

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
            if element_list[right_idx + 1 - num_index_popped].depth == element_list[right_idx + 1 - num_index_popped + 1].depth:
                new_depth_param = -1
            else:
                new_depth_param = 0
            element_list.insert(0, Element(value=0, depth=element_list[right_idx + 1 - num_index_popped].depth + new_depth_param))
            num_index_popped -= 1
        elif right_idx == len(element_list) - 1:
            print("No explode since last element")
            element_list[left_idx - 1].value += left_element.value
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1
            element_list.pop(right_idx - num_index_popped)
            num_index_popped += 1
            if element_list[left_idx - num_index_popped].depth < left_element.depth:
                new_depth_param = -1
            else:
                new_depth_param = 1
            element_list.append(Element(value=0, depth=element_list[left_idx - num_index_popped].depth))
            num_index_popped -= 1
        else:
            element_list[left_idx - 1].value += left_element.value
            element_list[right_idx + 1].value += right_element.value
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
    # return "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    # return "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
    # return "[[6,[5,[4,[3,2]]]],1]"
    # return "[[6,[5,[[3,2],4]]],1]"
    # [[6,[8,[0,6]]],1]
    return "[1,1]"


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
    explode_d, explode_index = explode_depth(input_list)
    split_d, split_index = split_depth(input_list)

    if split_index > explode_index:
        return split(input_list)
    elif split_index < explode_index:
        return explode(input_list)
    else:
        if split_d > explode_d:
            return split(input_list)
        elif split_d < explode_d:
            return explode(input_list)
        else:
            return False



def split_depth(element_list: list[Element]) -> (int, int):
    item_above_nine = list(filter(lambda x: x[1].value >= 10, enumerate(element_list)))
    if len(item_above_nine) == 0:
        return -1, -1
    return item_above_nine[0][1].depth, item_above_nine[0][0]


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


def add(input_list: list[Element], new_list: list[Element]):
    for e in input_list + new_list:
        e.depth += 1

    input_list.extend(new_list)


def show_list(input_list: list[Element]):
    for e in input_list:
        print(e)


def main():
    input = [
        "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
        "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"
    ]

    default_list = parse(input[0])
    # initial [[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # explode [[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # explode [[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # explode [[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # split   [[[[4,0],[5,4]],[[7,0],[[7,8],5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # explode [[[[4,0],[5,4]],[[7,7],[0,13]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # split   [[[[4,0],[5,4]],[[7,7],[0,[6,7]]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    # default_list = parse("[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]")
    # after explode [[[[0,[3,2]],[3,3]],[4,4]],[5,5]]
    # after explode [[[[3,0],[5,3]],[4,4]],[5,5]]
    # default_list = parse("[[[[0,[1,[2,2]]]],2],3],4]")
    # [[[[0,[1,[2,2]]],2],3],4]
    # [[[[0,[3,0]],4],3],4]
    # [[[[3,0],4],3],4]
    # after explode "[[5,5],[[4,4],[[3,5],[3,0]]]]"
    # after explode "[[5,5],[[4,4],[[3,5],[3,0]]]]"

    for e in input[1:]:
        # print(f"Input: {e}")
        new_list = parse(e)
        add(default_list, new_list)
        show_list(default_list)
        while step(default_list):
            print()
            show_list(default_list)
            print("Done")
            pass
    print()
    show_list(default_list)



if __name__ == '__main__':
    main()