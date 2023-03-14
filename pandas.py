import pandas as pd
import numpy as np

step_data = [3620, 7891, 9761, 3907, 4338, 5357]

#step_counts = pd.Series(step_data, name='steps')

step_counts.index = pd.date_range('20150329', periods=6)

print(step_counts)

print(step_counts["2015-04-01"])

print(step_counts[3])

print(step_counts["2015-04"])

print(step_counts.dtypes)

step_counts = step_counts.astype(np.float64)

print(step_counts.dtypes)

step_counts[1:3] = np.NaN

#step_counts = step_counts.fillna(0.)

print(step_counts[1:3])