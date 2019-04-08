#!/usr/bin/env python
import sys

import matplotlib.pyplot as plt
from sklearn import metrics, tree, neighbors, ensemble

from prep_terrain_data import makeTerrainData
from class_vis import scatter_plot, decision_boundry_plot


CLASSIFIERS = {
    'Decision Tree': tree.DecisionTreeClassifier(),
    'k-Nearest Neighbors': neighbors.KNeighborsClassifier(
        n_neighbors=15),
    'Random Forest': ensemble.RandomForestClassifier(
        n_estimators=10),
    'Ada Boost': ensemble.AdaBoostClassifier(),
}


def main():
    (features_train, labels_train,
     features_test, labels_test) = makeTerrainData()

    figures = []
    for title, clf in CLASSIFIERS.items():
        figures.append(plt.figure())
        clf.fit(features_train, labels_train)
        accuracy = metrics.accuracy_score(
            labels_test,
            clf.predict(features_test))
        plt.title(title + ' %s' % accuracy)
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
        plt.show(block=False)

    input('Press enter to close graphs')

    for figure in figures:
        plt.close(figure)


if __name__ == "__main__":
    sys.exit(main())
