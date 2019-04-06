#!/usr/bin/python

"""
This is the code to accompany the Lesson 3 (decision tree) mini-project.

Use a Decision Tree to identify emails from the Enron corpus by author:
Sara has label 0
Chris has label 1
"""

import sys
from tools.email_preprocess import preprocess

from sklearn import tree
from sklearn.metrics import accuracy_score


def main():
    (features_train, features_test,
     labels_train, labels_test) = preprocess(percentile=1)
    print('num_features:', len(features_test[0]))
    clf = tree.DecisionTreeClassifier(min_samples_split=40)
    clf.fit(features_train, labels_train)
    labels_predict = clf.predict(features_test)
    print('accuracy:', accuracy_score(labels_predict, labels_test))


if __name__ == "__main__":
    sys.exit(main())
