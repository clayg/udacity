import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import base64
import json


def draw_features(features_fast, features_slow):
    """
    Given the two collectoins of features draw them as a scatter graph on the
    global plt in blue and red.

    :param features_fast: a list of [x, y] points (blue)
    :param features_slow: a list of [x, y] points (red)
    """
    # our training features are (x, y) points, we need [x,...] & [y,...] lists
    # to scatter plot  - welcome to data science people!!!
    bumpy_fast, grade_fast = zip(*features_fast)
    bumpy_slow, grade_slow = zip(*features_slow)
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")


def prettyPicture(clf, X_test, y_test, filename=None):
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

    # Plot also the test points
    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test))
                 if y_test[ii] == 0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test))
                 if y_test[ii] == 0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test))
                 if y_test[ii] == 1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test))
                 if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")

    if filename:
        plt.savefig(filename)


def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print(image_start + json.dumps(data) + image_end)
