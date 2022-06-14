import pandas as pd # import library 
df = pd.read_csv("diabetes.csv") #load data diabetes.csv

df.loc[0:5, ['Glucose', 'BloodPressure', 'Age', 'Outcome']]
df.iloc[0:5, [0, 1, 5]]
df[['Glucose', 'BloodPressure', 'Age', 'Outcome']][:5]
df[:5][['Glucose','BloodPressure', 'Age', 'Outcome']]