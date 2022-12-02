from itertools import combinations
with open("data/day_02.txt") as f:
    data = f.read()

rows = data.split("\n")

total_distance = 0
ribbow_distance = 0
row_values = []

for row in rows:
    numbers = list(map(int, row.split("x")))
    numbers.sort()

    ribbow_distance += sum(numbers[0:2])*2 + (numbers[0] * numbers[1] * numbers[2])

    combs = list(combinations(numbers, 2))#
    products = list(map(lambda x: x[0] * x[1], combs))
    slack = min(products)
    value = sum(list(map(lambda x: 2 * x, products)))
    row_values.append(value + slack)

print(f"Part One: {sum(row_values)}")
print(f"Part Two: {ribbow_distance}")

