#!/usr/bin/env python
import sys

import matplotlib.pyplot as plt
from sklearn import metrics, neighbors

from tools.prep_terrain_data import makeTerrainData
from tools.class_vis import scatter_plot, decision_boundry_plot


CLASSIFIER_OPTS = [
    {'weights': 'distance', 'n_neighbors': 7},
    {'weights': 'distance', 'n_neighbors': 8},
    {'weights': 'distance', 'n_neighbors': 15},
    {'weights': 'distance', 'n_neighbors': 16},
    {'weights': 'uniform', 'n_neighbors': 21},
    {'weights': 'uniform', 'n_neighbors': 22},
    {'weights': 'uniform', 'n_neighbors': 23},
]


def main():
    (features_train, labels_train,
     features_test, labels_test) = makeTerrainData()

    best_accuracy = 0
    winner = None
    for opts in CLASSIFIER_OPTS:
        title = ','.join('%s=%s' % (k, v) for (k, v) in opts.items())
        clf = neighbors.KNeighborsClassifier(**opts)
        clf.fit(features_train, labels_train)
        accuracy = metrics.accuracy_score(
            labels_test,
            clf.predict(features_test))
        print(title, accuracy)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            winner = (title, clf)
    title, clf = winner
    plt.title(title + ' %s' % best_accuracy)
    decision_boundry_plot(clf)
    scatter_plot(features_train, labels_train, {
        0: {'c': 'b', 'label': 'train_fast'},
        1: {'c': 'r', 'label': 'train_slow'},
    })
    scatter_plot(features_test, labels_test, {
        0: {'c': 'g', 'label': 'test_fast'},
        1: {'c': 'y', 'label': 'test_slow'},
    })

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sys.exit(main())
