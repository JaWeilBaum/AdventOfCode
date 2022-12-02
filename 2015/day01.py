with open("data/day_01.txt") as f:
    data = f.read()

print(data)
up = data.count('(')
down = data.count(')')
print(f"Part One: {up - down}")

current_floor = 0

for index, char in enumerate(data):
    if char == '(':
        current_floor += 1
    else:
        current_floor -= 1
    if current_floor == -1:
        print(f"Part Two: {index + 1}")
        break
