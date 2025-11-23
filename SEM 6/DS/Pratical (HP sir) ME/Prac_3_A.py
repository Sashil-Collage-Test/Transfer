import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


df = pd.read_csv(r"C:\Users\DELL\Downloads\fetch_california_housing.csv")
df.head()

df.tail()

df.shape

df.size

df.describe()

df.info()

df.dtypes

housing = fetch_california_housing()

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df.head()

housing_df['PRICE']=housing.target
X=housing_df[['AveRooms']]
y=housing_df[['PRICE']]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,
                                               random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)


mse=mean_squared_error(y_test,model.predict(X_test))
r2=r2_score(y_test,model.predict(X_test))


print("Mean Squared Error: ", mse)
print("R-squared: ",r2)
print("Intercept: ",model.intercept_)
print("Co-efficient: ",model.coef_)
