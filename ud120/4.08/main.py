#! /usr/bin/env python
import sys

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

from prep_terrain_data import makeTerrainData
from ClassifyDT import classify


def simple_plot(features, labels, colors, show=False):
    x, y = zip(*features)
    c = [colors[int(i)] for i in labels]
    plt.scatter(x, y, c=c)
    if show:
        plt.show()


def calc_accuracy(true_labels, predicted_lables):
    correct = sum(i == j for i, j in zip(true_labels, predicted_lables))
    return correct / len(true_labels)


def main():
    (training_features, training_lables,
     test_features, true_labels) = makeTerrainData()
    classifier = classify(training_features, training_lables)
    predicted_lables = classifier.predict(test_features)

    simple_plot(training_features, training_lables, ['r', 'g'])
    simple_plot(test_features, predicted_lables, ['y', 'b'], show=True)

    print(accuracy_score(predicted_lables, true_labels))
    print(calc_accuracy(true_labels, predicted_lables))


if __name__ == "__main__":
    sys.exit(main())
