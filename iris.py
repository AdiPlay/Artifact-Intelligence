import pandas as pd
from sklearn.datasets import load_iris
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

iris = load_iris()
df = pd.DataFrame(iris['data'], columns = iris['feature_names'])
df['target'] = pd.Series(iris['target'], name = 'target_values')
df['target_name'] = df['target'].replace([0,1,2],
['iris-' + species for species in iris['target_names'].tolist()])
df.rename(columns={'target': 'labels'})
df.to_csv('tabelka.csv')
df