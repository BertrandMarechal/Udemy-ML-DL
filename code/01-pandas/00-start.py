import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Bertrand.Marechal/Documents/Projects/GitHubBertrand/Udemy-ML-DL/DataScience-Python3/PastHires.csv')

print(df.head(10))
print('yeah')
print(df.tail(4))
(rows, cols) = df.shape

print('Rows: ', rows)
print('Columns: ', cols)
print('Size: ', df.size)

print('Column names: ', df.columns)

print(df['Hired'][:5])
print(df[['Hired', 'Years Experience']][:5])
print(df.sort_values(['Years Experience']))

degreesCount = df['Level of Education'].value_counts()
print(degreesCount)
degreesCount.plot(kind='bar')

df2 = df[['Previous employers', 'Hired']][5:10]
print(df2)
# employer_counts = df2['Previous Employers'].value_counts()
# employer_counts.plot(kind='bar')