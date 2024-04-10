import os
import pandas as pd
from os import path
import numpy as np
from prettytable import PrettyTable     # https://pypi.org/project/prettytable/

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score, KFold
from scipy.stats import randint

# https://www.datacamp.com/tutorial/random-forests-classifier-python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.multioutput import MultiOutputClassifier

# https://seaborn.pydata.org/
import seaborn as sns
import matplotlib.pyplot as plt

path = os.getcwd().replace('/tfidf-wordclouds', '/flair')
text_features = pd.read_csv(path + "/home/training_data.csv")
text_features_header = list(text_features.columns)

text_features
text_features.shape

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

X = text_features.drop(columns=['Unnamed: 0', 'Book Title', 'MIN', 'MAX'])
y = text_features[['MIN', 'MAX']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# scaler here
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf = RandomForestClassifier(n_estimators=274, max_depth=17, random_state=42)

multi_output_rf = MultiOutputClassifier(rf)
multi_output_rf.fit(X_train_scaled, y_train)
y_train_pred = multi_output_rf.predict(X_train_scaled)
rf_pred = multi_output_rf.predict(X_test_scaled)

# tried to do kfold,,, dk if appropriate
folds = 5
kf = KFold(n_splits=folds, shuffle=True, random_state=13)
results = cross_val_score(multi_output_rf, X, y, cv=kf)

# test pred table
print(gen_table(rf_pred, X_test.index))

# PERFORMANCE REPORTS
# PERFORMANCE REPORTS
# PERFORMANCE REPORTS

print('-------------------------------------------------------')
print('Performance Metrics')
print('-------------------------------------------------------')
training_accuracy = accuracy_score(y_train.values.ravel(), y_train_pred.ravel()) * 100
print("Training Accuracy:", training_accuracy)

test_accuracy = accuracy_score(y_test.values.ravel(), rf_pred.ravel()) * 100
print("Test Accuracy:", test_accuracy)

print(f'Cross-Validation Results (Accuracy): ')
fold = 1
for value in results:
    print(f"Fold {fold}: {value}")
    fold += 1

# before HPT 59.272727
# after HPT  62.909090
print(f'Mean Accuracy: {(results.mean()) * 100}')

print('-------------------------------------------------------')

# classification report, MIN
print("Classification Report for MIN:")
print(classification_report(y_test['MIN'], rf_pred[:, 0]))
conf_matrix_min = confusion_matrix(y_test['MIN'], rf_pred[:, 0])
print("Confusion Matrix for MIN:")
print(conf_matrix_min)

print('-------------------------------------------------------')

# classification report, MAX
print("Classification Report for MAX:")
print(classification_report(y_test['MAX'], rf_pred[:, 1]))
conf_matrix_max = confusion_matrix(y_test['MAX'], rf_pred[:, 1])
print("Confusion Matrix for MAX:")
print(conf_matrix_max)

# PERFORMANCE REPORTS
# PERFORMANCE REPORTS
# PERFORMANCE REPORTS

print('-------------------------------------------------------')
print('Performance Metrics')
print('-------------------------------------------------------')
training_accuracy = accuracy_score(y_train.values.ravel(), y_train_pred.ravel()) * 100
print("Training Accuracy:", training_accuracy)

test_accuracy = accuracy_score(y_test.values.ravel(), rf_pred.ravel()) * 100
print("Test Accuracy:", test_accuracy)

print(f'Cross-Validation Results (Accuracy): ')
fold = 1
for value in results:
    print(f"Fold {fold}: {value}")
    fold += 1

# before HPT 59.272727
# after HPT  62.909090
print(f'Mean Accuracy: {(results.mean()) * 100}')

print('-------------------------------------------------------')

# classification report, MIN
print("Classification Report for MIN:")
print(classification_report(y_test['MIN'], rf_pred[:, 0]))
conf_matrix_min = confusion_matrix(y_test['MIN'], rf_pred[:, 0])
print("Confusion Matrix for MIN:")
print(conf_matrix_min)

print('-------------------------------------------------------')

# classification report, MAX
print("Classification Report for MAX:")
print(classification_report(y_test['MAX'], rf_pred[:, 1]))
conf_matrix_max = confusion_matrix(y_test['MAX'], rf_pred[:, 1])
print("Confusion Matrix for MAX:")
print(conf_matrix_max)

rf = RandomForestClassifier(n_estimators=274, max_depth=17, random_state=42)

multi_output_rf = MultiOutputClassifier(rf)
multi_output_rf.fit(X_train_scaled, y_train)

selector = SelectFromModel(multi_output_rf.estimators_[0], threshold='mean')
selector.fit(X_train_scaled, y_train)
best = selector.get_support()[1:]

# feature selection: RF feature importance
feature_importances = []
for var in multi_output_rf.estimators_:
    feature_importances.append(var.feature_importances_)

avg_feature_importance = np.mean(feature_importances, axis=0)

features = text_features.columns[2:-2]
combined = zip(features, avg_feature_importance[1:])
for pair in list(combined):
    print(pair)

# saving model as a pickle
import pickle
pickle.dump(multi_output_rf,open("flair_model.sav", "wb"))
pickle.dump(scaler, open("scaler.sav", "wb"))