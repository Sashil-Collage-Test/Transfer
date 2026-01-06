import pandas as pd
import numpy as np
df=pd.read_csv("Prac_1_2_4_csv_Iris.csv")
print(df.head())
df.head()
df.tail()
df.describe()
df.info()
df.shape
df.dtypes
df.columns
missing_values=df.isnull().sum()
print("\nMissing values in csv data:")
print("Missing_values")
df=df.drop(columns=['Species'])
fill=df.fillna(df.mean())
print("\nFilled Missing Values with Mean (CSV Data):")
print(df.head())
z_scores=np.abs((fill-fill.mean())/fill.std())
z_scores
do=fill[(z_scores<3).all(axis=1)]
print("\nData After Removing Outliers (CSV Data):")
print(do.head())
threshold_value=3
filter=do[do['SepalLengthCm']>threshold_value]
print(f"\nFilterd Data(Rows with column_name>{threshold_value}):")
print(filter)
df_sorted=filter.sort_values(by='SepalWidthCm',ascending=False)
print(df_sorted.head())
df_grouped=df_sorted.groupby('SepalLengthCm').agg({'PetalLengthCm':'mean',
                                                   'PetalWidthCm':'sum'
                                                   }).reset_index()
print("\nGrouped Data (Mean and Sum for Each Group):")
print(df_grouped.head())
