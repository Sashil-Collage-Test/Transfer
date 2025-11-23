import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\DELL\Desktop\MSC Data science\Data sets\Iris.csv")
print(df.head()) # Display the first 5 rows of the DataFrame

df.head()
df.tail()
df.describe()
df.info()
df.shape
df.dtypes
df.columns


missing_values = df.isnull().sum()
print("\nMissing Values in CSV Data:")
print(missing_values)
df = df.drop(columns=['Species'])

fill= df.fillna(df.mean())
print("\nFilled Missing Values with Mean (CSV Data):")
print(df.head())


z_scores = np.abs((fill - fill.mean()) / fill.std())
z_scores

do = fill[(z_scores < 3).all(axis=1)]
print("\nData After Removing Outliers (CSV Data):")
print(do.head())

threshold_value = 3 # Example threshold value
filter = do[do['SepalLengthCm'] > threshold_value]
print(f"\nFiltered Data (Rows with column_name > {threshold_value}):")
print(filter)

df_sorted = filter.sort_values(by='SepalWidthCm', ascending=False)
print(df_sorted.head())

df_grouped = df_sorted.groupby('SepalLengthCm').agg({
    'PetalLengthCm': 'mean','PetalWidthCm': 'sum'}).reset_index()
print("\nGrouped Data (Mean and Sum for Each Group):")
print(df_grouped.head())
