import pandas as pd
from sklearn.preprocessing import LabelEncoder

iris=pd.read_csv(r"C:\Users\DELL\Desktop\MSC Data science\Data sets\Iris.csv")
iris

le=LabelEncoder()
iris['code']=le.fit_transform(iris.Species)
iris

