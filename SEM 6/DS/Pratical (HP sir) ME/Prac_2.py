import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv(r"C:\Users\DELL\Desktop\wine.csv")
df

df1 = pd.read_csv(r"C:\Users\DELL\Desktop\wine.csv", usecols=[0, 1, 2], skiprows=1
df1.columns = ['classlabel', 'Alcohol', 'Malic Acid']
print("Original DataFrame:")
df1

scaling=MinMaxScaler()
scaled_value=scaling.fit_transform(df1[['Alcohol','Malic Acid']])
df1[['Alcohol','Malic Acid']]=scaled_value
print("\n Dataframe after MinMax Scaling")
df1

