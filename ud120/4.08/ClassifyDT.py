from sklearn import tree


def classify(features_train, labels_train):
    classifier = tree.DecisionTreeClassifier(min_samples_split=5)
    classifier.fit(features_train, labels_train)
    return classifier
