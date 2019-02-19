#!/usr/bin/env python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, draw_features

# your imports go here
from sklearn.svm import SVC


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
def filter_feature_for_label(features, labels, desired_label):
    return [feature for feature, label in zip(features, labels)
            if label == desired_label]


features_train, labels_train, features_test, labels_test = makeTerrainData()

features_fast = filter_feature_for_label(features_train, labels_train, 0)
features_slow = filter_feature_for_label(features_train, labels_train, 1)


# initial visualization
draw_features(features_fast, features_slow)
###############################################################################


# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

clf = SVC(C=10000.0, kernel="rbf")
clf.fit(features_train, labels_train)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

plt.show()
