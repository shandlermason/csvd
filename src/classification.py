import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedKFold
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import settings
from metrics import measure_final_score


def getMetrics(df, y_test, pred, keyword, learner='knn'):

    recall = measure_final_score(df, y_test, pred, keyword, 'recall')
    precision = measure_final_score(df, y_test, pred, keyword, 'precision')
    accuracy = measure_final_score(df, y_test, pred, keyword, 'accuracy')
    F1 = measure_final_score(df, y_test, pred, keyword, 'F1')
    AOD = measure_final_score(df, y_test, pred, keyword, 'aod')
    EOD =measure_final_score(df, y_test, pred, keyword, 'eod')
    SPD = measure_final_score(df, y_test, pred, keyword, 'SPD')
    FA0 = measure_final_score(df, y_test, pred, keyword, 'FA0')
    FA1 = measure_final_score(df, y_test, pred, keyword, 'FA1')
    DI = measure_final_score(df, y_test, pred, keyword, 'DI')

    return [recall, precision, accuracy, F1, FA0, FA1, AOD, EOD, SPD, DI, learner]


def main():
    datasets = ['https://raw.githubusercontent.com/laurensalvarez/Lying/main/datasets/processed/diabetes_p.csv']
        #, "heart", "germancredit", "diabetes", "communities", "compas", "studentperformance", "bankmarketing", "defaultcredit", "adultscensusincome"]
    keywords = {'https://raw.githubusercontent.com/laurensalvarez/Lying/main/datasets/processed/diabetes_p.csv' : ['Age('],
                'adultscensusincome': ['race', 'sex'],
                'compas': ['race', 'sex'],
                'bankmarketing': ['Age'],
                'defaultcredit': ['sex'],
                'diabetes': ['Age'],
                'germancredit': ['sex'],
                'heart': ['Age'],
                'studentperformance': ['sex']
                }

    for dataset in datasets:
        klist = keywords[dataset]
        results = []
        for keyword in klist:

            # import data
            rows = settings.csv_function(dataset)
            columns = rows[0]
            rows.pop(0)
            df = pd.DataFrame(rows, columns=columns)
            # from dataframe split into X and Y
            y = df["!probability"].values
            # remove y values from df
            df.drop('!probability', axis=1)
            X = df.values

            # repeated k fold - 5x5
            '''Split dataset into k consecutive folds (without shuffling by default). Each fold is then used 
            once as a validation while the k - 1 remaining folds form the training set'''
            rkf = RepeatedKFold(n_splits=5, n_repeats=5, random_state=10039)
            for train_index, test_index in rkf.split(X):
                # print("TRAIN:", train_index, "TEST:", test_index)
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y[train_index], y[test_index]

                # create new df from train index
                train_df = pd.DataFrame(X_test, columns=df.columns)
                # implement my own stuff later
                # implement classifier (clf)
                clf = KNeighborsClassifier(n_neighbors=3)
                # training = fitting, fit classifier to training data
                clf.fit(X_train, y_train)
                # have a fully trained classifier
                # predict classes for set you haven't seen yet (test values)
                pred = clf.predict(X_test)  # returns list of class labels (predictions)
                # compare predictions to actual ground truth value

                results.append(getMetrics(train_df, y_test, pred, keyword))

    pd.DataFrame(results, columns=['recall', 'precision', 'accuracy', 'F1', 'FA0', 'FA1', 'AOD', 'EOD', 'SPD', 'DI', 'learner']).to_csv("output.csv", index=False)

if __name__ == "__main__":
    main()


