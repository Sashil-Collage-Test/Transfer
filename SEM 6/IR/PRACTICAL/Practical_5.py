import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

df=pd.read_csv("Prac_5_data1.csv")
data=df["covid"]+""+df["fever"]
X=data.astype(str)
Y=df["flu"]

X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2, random_state=42)

vectorizer=CountVectorizer()
X_train_counts=vectorizer.fit_transform(X_train)
X_test_counts=vectorizer.transform(X_test)

classifier=MultinomialNB()
classifier.fit(X_train_counts, Y_train)

data1=pd.read_csv("Prac_5_data2.csv")
new_data=data1["covid"]+""+data1["fever"]
new_data_counts=vectorizer.transform(new_data.astype(str))
predictions=classifier.predict(new_data_counts)

new_data=predictions

accuracy=accuracy_score(Y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy:{accuracy:.2f}")
print(classification_report(Y_test, classifier.predict(X_test_counts)))

predictions_df=pd.DataFrame(predictions, columns=['flu_prediction'])
data1=pd.concat([data1, predictions_df], axis=1)
data1.to_csv("test_result.csv", index=False)
print("Predictions Saved to test_result.csv")
