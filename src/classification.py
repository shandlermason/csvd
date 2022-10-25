import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedKFold
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import settings



def main():
    # import data
    rows = settings.csv_function('https://raw.githubusercontent.com/senthusiast/Causality-Testing/main/data/processed.cleveland.data.csv')

    df = pd.DataFrame(rows)
    print(df.head())

    # from dataframe split into X and Y
    y = df["Probability"].values
    # remove y values from df
    df.drop('Probability', axis=1)
    X = df.values

    # repeated k fold - 5x5
    '''Split dataset into k consecutive folds (without shuffling by default). Each fold is then used 
    once as a validation while the k - 1 remaining folds form the training set'''
    rkf = RepeatedKFold(n_splits=5, n_repeats=5, random_state=10039)
    for train_index, test_index in rkf.split(X):
        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # implement my own stuff later
        # implement classifier (clf)
        clf = KNeighborsClassifier(n_neighbors=3)
        # training = fitting, fit classifier to training data
        clf.fit(X_train, y_train)
        # have a fully trained classifier
        # predict classes for set you haven't seen yet (test values)
        pred = clf.predict(X_test)  # returns list of class labels (predictions)
        # compare predictions to actual ground truth value
        


    # compare to actual test values

    return 0





if __name__ == "__main__":
    main()


