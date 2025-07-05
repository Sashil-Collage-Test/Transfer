import numpy as np
import pandas as pd
PlayTennis= pd.read_csv("C:/Shashikant (highly volatile)/CODEING/SEM_5/AI/Pratical_3&4/PlayTennis.csv") 

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

from sklearn import tree 

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
