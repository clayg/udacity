#!/usr/bin/python
import random


def makeTerrainData(n_points=1000):
    """
    make the toy dataset
    """
    random.seed(42)
    grade = [random.random() for ii in range(0, n_points)]
    bumpy = [random.random() for ii in range(0, n_points)]
    error = [random.random() for ii in range(0, n_points)]
    # make some noisy data along the slow
    labels = [round(grade[ii] * bumpy[ii] + 0.3 + 0.1 * error[ii])
              for ii in range(0, n_points)]
    # round off the edges, slow down if it's high grade or really bumpy
    for g, b, label_index in zip(grade, bumpy, range(len(labels))):
        if g > 0.8 or b > 0.8:
            labels[label_index] == 1.0

    # build feature set
    features = [(x, y) for x, y in zip(grade, bumpy)]

    # split into train/test sets
    split_index = int(0.75*n_points)
    features_train = features[0:split_index]
    labels_train = labels[0:split_index]
    features_test = features[split_index:]
    labels_test = labels[split_index:]

    return features_train, labels_train, features_test, labels_test
