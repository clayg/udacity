import numpy as np
import matplotlib.pyplot as plt


def scatter_plot(features, labels, details):
    """
    Do a scatter plot of points with boolean labels.

    :param features: a list of (x, y) points
    :param labels: a list of labels for each point
    :param details: a map of label to color and legend context
    """
    (x, y), = np.dstack(features)
    labels = np.array(labels)
    for i, ctx in details.items():
        s = np.where(labels == i)
        plt.scatter(x[s], y[s], **ctx)


def decision_boundry_plot(clf):
    """
    We make a "grid" of every point in the graph and make a prediction and plot
    the results
    """
    steps = np.arange(0.0, 1.1, 0.01)
    x, y = np.meshgrid(steps, steps)
    map_features = np.c_[x.ravel(), y.ravel()]
    graph_labels = clf.predict(map_features)
    c = graph_labels.reshape(x.shape)
    plt.pcolormesh(x, y, c, cmap=plt.get_cmap('seismic'))


def prettyPicture(clf, features_test, labels_test):
    plt.close()
    decision_boundry_plot(clf)
    scatter_plot(features_test, labels_test, {
        0: {'c': 'b', 'label': 'test_fast'},
        1: {'c': 'r', 'label': 'test_slow'},
    })

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.legend()
    plt.show()
