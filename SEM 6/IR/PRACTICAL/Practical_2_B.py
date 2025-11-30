from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
import numpy as np
from numpy.linalg import norm

train_set=["The sky is blue.","The sun is bright."]
test_set=["The sun in the sky is bright."]

vectorizer=CountVectorizer(stop_words="english")
transformer=TfidfTransformer()

train_vectors=vectorizer.fit_transform(train_set).toarray()
test_vectors=vectorizer.transform(test_set).toarray()

print("Training Set TF-IDF:",train_vectors)
print("Test Set TF-IDF:",test_vectors)

def cosine_similarity(vec1,vec2):
    return round(np.dot(vec1,vec2)/(norm(vec1)*norm(vec2)),3)

for train_vec in train_vectors:
    for test_vec in test_vectors:
        print("Cosin Similarity:",cosine_similarity(train_vec,test_vec))
