import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

playtennis = pd.read_csv("playtennis.csv")
le = LabelEncoder()
print("Original DataFrame:\n", playtennis, "\n")

playtennis['Outlook'] = le.fit_transform(playtennis['Outlook'])
playtennis['Temperature'] = le.fit_transform(playtennis['Temperature'])
playtennis['Humidity'] = le.fit_transform(playtennis['Humidity'])
playtennis['Wind'] = le.fit_transform(playtennis['Wind'])
playtennis['Play Tennis'] = le.fit_transform(playtennis['Play Tennis'])

y = playtennis['Play Tennis']
X = playtennis.drop(['Play Tennis'], axis=1)

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, y)
print("Decision Tree Text Representation:\n", tree.export_text(clf, feature_names=list(X.columns)))

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
