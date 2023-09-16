import pandas as pd

print('Pandas')

a = [1, 7, 3]
v = pd.Series(a, index=['x', 'y', 'z'])
print(v)