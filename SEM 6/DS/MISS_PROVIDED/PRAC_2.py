#Feature Scaling
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
df=pd.read_csv("Prac2_csv_wine.csv")
print("\nFull CSV Loaded:")
print(df.head())
df1=pd.read_csv("Prac2_csv_wine.csv", usecols=[0,1,2], skiprows=1)
df1.columns=['classlabel','Alcohol','Malic Acid']
print("\nOriginal DataFrame (First 5 Rows):")
print(df1.head())
scaling=MinMaxScaler()
scaled_value=scaling.fit_transform(df1[['Alcohol','Malic Acid']])
df1[['Alcohol','Malic Acid']]=scaled_value
print("\nDataframe After Min-Max Scaling:")
print(df1.head())
scaling=StandardScaler()
scaled_standardvalue=scaling.fit_transform(df1[['Alcohol','Malic Acid']])
df1[['Alcohol','Malic Acid']]=scaled_standardvalue
print("\nDataframe After Standard Scaling:")
print(df1.head())
plt.scatter(df1['Alcohol'],df1['Malic Acid'])
plt.title("Standard Scaled Alcohol vs Malic Acid")
plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.show()

#Feature Dummification
ir_is=pd.read_csv("Prac_1_2_4_csv_Iris.csv")
ir_is
le=LabelEncoder()
ir_is['code']=le.fit_transform(ir_is.Species)
ir_is
