import os
import pandas as pd
from os import path
import numpy as np
from prettytable import PrettyTable     # https://pypi.org/project/prettytable/


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.multioutput import MultiOutputClassifier

#LR libraries
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

# Example corpus
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer to the corpus and transform the documents into TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Print the shape of the TF-IDF matrix
print("TF-IDF Matrix Shape:", tfidf_matrix.shape)

# Get the feature names (words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Print the feature names
print("Feature Names:", feature_names)

# Print the TF-IDF matrix
print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())


# path = os.getcwd()
# text_features = pd.read_csv(path + "/book.csv")
# text_features_header = list(text_features.columns)
# print(text_features)

# # fx generates prettytable instances

# def gen_table(prediction, tests):

#     data = []
#     i = 0
#     book_titles = tests

#     for test in book_titles:
#         unit = []
#         unit.append(text_features.loc[test]['Book Title'])
#         unit.append(prediction[i][0])
#         unit.append(prediction[i][1])
#         data.append(unit)
#         i += 1

#     table = PrettyTable()
#     table.title = 'Test Predictions'
#     table.field_names = ['Test Title', 'Min Age', 'Max Age']
#     table.align['Test Title'] = 'l'
    
#     for row in data:
#         table.add_row(row)

#     return table

# X = text_features.drop(columns=['Book Title', 'MIN', 'MAX'])
# y = text_features[['MIN', 'MAX']]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# logreg = LogisticRegression(max_iter=1000, penalty='l2')
# multi_logreg = MultiOutputClassifier(logreg)
# multi_logreg.fit(X_train_scaled, y_train)

# lr_pred = multi_logreg.predict(X_test_scaled)

# print(gen_table(lr_pred, X_test.index))

# print('-------------------------------------------------------------------------------------------------')
# print('Statistics')
# print('-------------------------------------------------------------------------------------------------')
# accuracy = accuracy_score(y_test.values.ravel(), lr_pred.ravel())
# conf_matrix = confusion_matrix(y_test.values.ravel(), lr_pred.ravel())
# print("Accuracy:", accuracy)
# print(f'Confusion Matrix:\n{conf_matrix}')

