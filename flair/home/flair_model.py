import os
import pandas as pd
from os import path
import numpy as np
from prettytable import PrettyTable     # https://pypi.org/project/prettytable/

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_selection import SelectFromModel

from sklearn.preprocessing import StandardScaler

#RF libraries
# source - https://www.datacamp.com/tutorial/random-forests-classifier-python
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

# https://seaborn.pydata.org/
import seaborn as sns
import matplotlib.pyplot as plt


# fx generates prettytable instances
def gen_table(prediction, tests):

    data = []
    i = 0
    book_titles = tests

    for test in book_titles:
        unit = []
        unit.append(text_features.loc[test]['Book Title'])
        unit.append(prediction[i][0])
        unit.append(prediction[i][1])
        data.append(unit)
        i += 1

    table = PrettyTable()
    table.title = 'Test Predictions'
    table.field_names = ['Test Title', 'Min Age', 'Max Age']
    table.align['Test Title'] = 'l'
    
    for row in data:
        table.add_row(row)

    return table



#get extracted text features
path = os.getcwd()
text_features = pd.read_csv(path + "/home/training_data.csv")
text_features_header = list(text_features.columns)

X = text_features.drop(columns=['Book Title', 'MIN', 'MAX'])
y = text_features[['MIN', 'MAX']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# scale extracted data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# RANDOM FOREST CLASSIFIER
rf = RandomForestClassifier(n_estimators=100, random_state=42)

multi_output_rf = MultiOutputClassifier(rf)
multi_output_rf.fit(X_train_scaled, y_train)
rf_pred = multi_output_rf.predict(X_test_scaled)

# feature selection: RF feature importance
feature_importances = []
for var in multi_output_rf.estimators_:
    feature_importances.append(var.feature_importances_)

avg_feature_importance = np.mean(feature_importances, axis=0)

features = text_features.columns[2:-2]
combined = zip(features, avg_feature_importance[1:])
#for pair in list(combined):
    #print(pair)


# accuracy results
#print(gen_table(rf_pred, X_test.index))

#print('-------------------------------------------------------------------------------------------------')
#print('Statistics')
#print('-------------------------------------------------------------------------------------------------')
rf_accuracy = accuracy_score(y_test.values.ravel(), rf_pred.ravel())
conf_matrix = confusion_matrix(y_test.values.ravel(), rf_pred.ravel())
#print("Accuracy:", rf_accuracy)
#print(f'Confusion Matrix:\n{conf_matrix}') """

sns.heatmap(conf_matrix, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)


# saving model as a pickle
import pickle
pickle.dump(multi_output_rf,open("flair_model.sav", "wb"))
pickle.dump(scaler, open("scaler.sav", "wb"))