import pandas as pd

step_data = [3620, 7891, 9761, 3907, 4338, 5357]

#step_counts = pd.Series(step_data, name='steps')

step_counts.index = pd.date_range('20150329', periods=6)

print(step_counts)