from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas
import os
from os import path
import numpy as np

#SOURCE: https://stackoverflow.com/questions/54820210/how-to-train-svm-model-in-sklearn-python-by-input-csv-file
#SOURCE: https://databasetown.com/implementing-support-vector-machine-svm-in-python/
path = path = os.getcwd()
text_features = pandas.read_csv(path + "/extracted_TRAD_LEX.csv")
text_features_header = ["Word Count", "Sentence Count", "Ave. Word Length", "Ave. Sentence Length", "Total Syllables", "Noun-Token Ratio",
                        "Verb-Token Ratio", "Type-Token Ratio", "Root TTR", "Corrected TTR", "Bilogarithmic TTR", "Lexical Density",
                        "FW-Token Ratio", "Age Classification"]


X = text_features[text_features_header[:-1]].values
Y = text_features[['Age Classification']].values.ravel()

label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)
X = StandardScaler().fit_transform(X)

x_train , x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=7)

model = SVC(kernel='rbf', random_state = 1).fit(x_train,y_train)

check_accuracy = model.score(x_test, y_test)
print("Accuracy: ", check_accuracy)