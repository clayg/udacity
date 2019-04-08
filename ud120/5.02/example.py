#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData

from sklearn import tree

from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors in
# the scatterplot and identify them visually
grade_fast = [features_train[i][0] for i in range(0, len(features_train))
              if labels_train[i] == 0]
bumpy_fast = [features_train[i][1] for i in range(0, len(features_train))
              if labels_train[i] == 0]
grade_slow = [features_train[i][0] for i in range(0, len(features_train))
              if labels_train[i] == 1]
bumpy_slow = [features_train[i][1] for i in range(0, len(features_train))
              if labels_train[i] == 1]


# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
##############################################################################

# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)


try:
    clf
except NameError:
    pass
else:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
