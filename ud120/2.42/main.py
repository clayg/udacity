#! /usr/bin/env python
import sys
import time

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from tools.email_preprocess import preprocess


def main():
    features_train, features_test, labels_train, labels_test = preprocess()

    clf = GaussianNB()
    start = time.time()
    clf.fit(features_train, labels_train)
    delta_fit = time.time() - start
    print(f'Training complete in {delta_fit:.2f}s')

    start = time.time()
    labels_predict = clf.predict(features_test)
    delta_predict = time.time() - start
    print(f'Prediction complete in {delta_predict:.2f}s')

    score = accuracy_score(labels_predict, labels_test)
    print(f'Accuracy {100 * score:.2f}%')


if __name__ == "__main__":
    sys.exit(main())
