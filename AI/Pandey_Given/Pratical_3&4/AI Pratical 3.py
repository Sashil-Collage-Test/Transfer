import numpy as np
import pandas as pd
from sklearn import tree 

PlayTennis= pd.read_csv("PlayTennis.csv")
print(PlayTennis,"\n\n")

from sklearn.preprocessing import LabelEncoder
Le= LabelEncoder()

PlayTennis['Outlook']=Le.fit_transform(PlayTennis['Outlook'])
PlayTennis['Temperature']=Le.fit_transform(PlayTennis['Temperature']) 
PlayTennis['Humidity']=Le.fit_transform(PlayTennis['Humidity']) 
PlayTennis['Wind']=Le.fit_transform(PlayTennis['Wind']) 
PlayTennis['Play Tennis']=Le.fit_transform(PlayTennis['Play Tennis']) 
print(PlayTennis,"\n\n")

y=PlayTennis['Play Tennis']
X=PlayTennis.drop(['Play Tennis'], axis=1) 

clf=tree.DecisionTreeClassifier(criterion='entropy') 
clf=clf.fit(X, y) 

print(tree.plot_tree(clf),"\n\n") 

import graphviz
dot_data=tree.export_graphviz(clf, out_file=None) 
graph=graphviz.Source(dot_data)
print(graph)
 # python shell can't print graph image so, it will print the code for diagraph implementation

X_pred=clf.predict(X)
print(X_pred==y,"\n")

import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10))  
tree.plot_tree(
    clf,
    feature_names=X.columns,
    class_names=['No', 'Yes'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree Visualization (Matplotlib)")
plt.show()
