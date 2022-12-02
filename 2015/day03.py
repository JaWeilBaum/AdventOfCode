import pandas as pd
import hashlib

with open("data/day_03.txt") as f:
    data = f.read()

print(data)

def hash_coords(x, y) -> str:
    return hashlib.sha512(f"{x}-{y}".encode("utf-8")).hexdigest()

current_x = 0
current_y = 0

robo_x = 0
robo_y = 0

santa_x = 0
santa_y = 0

location_hashes = [{"hash": hash_coords(current_x, current_y), "split_hash": hash_coords(current_x, current_y)}]

for index, move in enumerate(data):
    x_value = 0
    y_value = 0
    if move == 'v':
        y_value = -1
    elif move == '^':
        y_value = 1
    elif move == '<':
        x_value = -1
    elif move == '>':
        x_value = 1
    else:
        break

    current_x += x_value
    current_y += y_value

    new_data = {"hash": hash_coords(current_x, current_y)}

    if index % 2 == 0:
        santa_x += x_value
        santa_y += y_value
        new_data["split_hash"] = hash_coords(santa_x, santa_y)
    else:
        robo_x += x_value
        robo_y += y_value
        new_data["split_hash"] = hash_coords(robo_x, robo_y)
    location_hashes.append(new_data)


df = pd.DataFrame(location_hashes)
print(f"Part One: {len(df.groupby('hash', as_index=False).hash.count())}")
print(f"Part Two: {len(df.groupby('split_hash').split_hash.count())}")