import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
df=pd.read_csv("Prac3_csv_FCH.csv")
print("\nCSV Data Loaded:")
print(df.head())
print(df.tail())
print("Shape:",df.shape)
print("Size:",df.size)
print(df.describe())
print(df.info())
print("\nData Types:\n",df.dtypes)
housing=fetch_california_housing()
housing_df=pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df["PRICE"]=housing.target
print(housing_df.head())


X=housing_df[['AveRooms']]
y=housing_df[['PRICE']]
X_train, X_test, y_train, y_test=train_test_split(
    X, y, test_size=0.2, random_state=42
    )
model=LinearRegression()
model.fit(X_train, y_train)
mse=mean_squared_error(y_test,model.predict(X_test))
r2=r2_score(y_test,model.predict(X_test))
print("\n========SIMPLE LINEAR REGRESSION=======")
print("Mean Squared Error:",mse)
print("R-squared Value:",r2)
print("Intercept:",model.intercept_)
print("Coefficien:",model.coef_)


X=housing_df.drop("PRICE",axis=1)
y=housing_df["PRICE"]
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2, random_state=42
    )
model=LinearRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
mse=mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
print("\n=========MULTIPLE LINEAE REGRESSION=========")
print("Mean Squared Error:",mse)
print("R-squared Value:",r2)
print("Intercept:",model.intercept_)
print("Coefficients:",model.coef_)
