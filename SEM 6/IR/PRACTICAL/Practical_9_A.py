import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=np.array([[1,2],[2,3],[3,3],[4,5],[5,5],[6,7]])
y=np.array([0,0,1,1,2,2])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

model=SVC(kernel="linear",probability=True)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
