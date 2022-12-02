import pandas as pd
import numpy as np

df = pd.read_csv("../../data/day_01.txt", header=None, skip_blank_lines=False)
# Split into blocks
splits = np.split(df, df[df[0].isna()].index)
values = sorted(list(map(lambda x: x[0].sum(), splits)), reverse=True)
print(f"Part 1: {values[0]}")
print(f"Part 2: {sum(values[0:3])}")