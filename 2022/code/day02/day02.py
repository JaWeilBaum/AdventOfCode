import pandas as pd

df = pd.read_csv("../../data/day_02.txt", header=None)
df.columns = ["input"]
df["part_one_shape"] = df.input.replace(to_replace={"A X": 1, "B X": 1, "C X": 1, "A Y": 2, "B Y": 2, "C Y": 2, "A Z": 3, "B Z": 3, "C Z": 3})
df["part_one_result"] = df.input.replace(to_replace={"A Z": 0, "B X": 0, "C Y": 0, "A X": 3, "B Y": 3, "C Z": 3, "A Y": 6, "B Z": 6, "C X": 6})
df["part_two_shape"] = df.input.replace(to_replace={"A X": 3, "B X": 1, "C X": 2, "A Y": 1, "B Y": 2, "C Y": 3, "A Z": 2, "B Z": 3, "C Z": 1})
df["part_two_result"] = df.input.replace(to_replace={"A X": 0, "B X": 0, "C X": 0, "A Y": 3, "B Y": 3, "C Y": 3, "A Z": 6, "B Z": 6, "C Z": 6})
print(f"Part One: Total score: {(df.part_one_shape + df.part_one_result).sum()}")
print(f"Part Two: Total score: {(df.part_two_shape + df.part_two_result).sum()}")
# print(df)
