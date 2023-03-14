import pandas as pd

step_data = [3620, 7891, 9761, 3907, 4338, 5357]

step_counts = pd.Series(step_data, name='steps')

print(step_counts)