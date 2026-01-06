import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
df=pd.read_csv("Prac1_csv_Iris.csv")
print("\nOriginal Dataset:")
print(df.head())
df=df[df['Species']!='Iris-virginica']
print("\nDataset After Removing Class 2:")
print(df.head())
x=df.drop('Species',axis=1)
y=df['Species']
x_train, x_test, y_train, y_test=train_test_split(
    x,y,test_size=0.2, random_state=42
    )
logistic_model=LogisticRegression()
logistic_model.fit(x_train, y_train)
y_pred_logistic=logistic_model.predict(x_test)
print("\n=======Logistic Regression Results======")
print("Accuracy:", accuracy_score(y_test, y_pred_logistic))
print("\nClassification Reprot:\n", classification_report(y_test, y_pred_logistic))


from sklearn.tree import DecisionTreeClassifier
x_train, x_test, y_train, y_test=train_test_split(
    x, y, test_size=0.2, random_state=42
    )
model=DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred_tree=model.predict(x_test)
print("\n=======Decision Tree Classifier Results=======")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("\nClassification Report:\n", classification_report(y_test, y_pred_tree))
