#! /usr/bin/env python
import sys
import time

from sklearn.metrics import accuracy_score

from tools.email_preprocess import preprocess

# your imports go here
from sklearn.svm import SVC


def find_best(features_train, features_test, labels_train, labels_test,
              n=None, **params):
    param_sets = []
    for C in (1.0, 10.0, 100.0, 1000.0, 10000.0):
        param_sets.append({
            'kernel': params.get('kernel', 'linear'),
            'gamma': params.get('gamma', 'scale'),
            'C': C,
        })

    accuracy_map = []
    for params in param_sets:
        print('=' * 70)
        score = do_test(
            features_train, features_test, labels_train, labels_test,
            n=n, **params)
        accuracy_map.append((score, params))

    for score, params in sorted(accuracy_map, key=lambda i: i[0]):
        print(f'{params} => {score}')


def do_test(features_train, features_test, labels_train, labels_test,
            n=None, **params):
    if n is not None:
        n = int(n)
    print(f'{params}')
    clf = SVC(**params)

    start = time.time()
    clf.fit(features_train[:n], labels_train[:n])
    delta_fit = time.time() - start
    print(f'Training complete in {delta_fit:.2f}s')

    start = time.time()
    labels_predict = clf.predict(features_test)
    delta_predict = time.time() - start
    print(f'Prediction complete in {delta_predict:.2f}s')
    print(f'10 => {labels_predict[10]}')
    print(f'26 => {labels_predict[26]}')
    print(f'50 => {labels_predict[50]}')
    print(f'Chris => {sum(labels_predict)}')

    score = accuracy_score(labels_predict, labels_test)
    print(f'Accuracy {100 * score:.2f}%')

    return labels_predict, score


def main():
    features_train, features_test, labels_train, labels_test = preprocess()
    do_test(features_train, features_test, labels_train, labels_test,
            kernel='rbf', gamma='auto', C=10000.0)


if __name__ == "__main__":
    sys.exit(main())
