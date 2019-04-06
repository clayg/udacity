import sys
import math


def entropy(labels):
    """
    Calculate the entropy of a given set of labels.

    :param labels: a list of booleans (1 or 0)
    """
    p1 = sum(labels) / len(labels)
    p0 = sum(not i for i in labels) / len(labels)
    return sum(-i * math.log2(i) for i in [p1, p0] if i)


def information_gain(parent, children):
    """
    What is the information gain of splitting parent into the given children

    :param parent: entropy of parent
    :param children: list of children labels
    """
    total_children = sum(len(c) for c in children)
    return parent - sum((len(c) / total_children) * entropy(c)
                        for c in children)


def main():
    print(entropy([1]))
    print(entropy([0]))
    print(entropy([1, 1, 1]))
    print(entropy([0, 0, 0]))
    print(entropy([1, 0, 0, 0]))
    print(entropy([0, 1, 1, 1]))
    print(entropy([0, 0, 1, 1]))
    print(entropy([1, 0, 1, 0]))

    print('=' * 25)
    print(information_gain(1.0, [[0, 1], [1, 0]]))
    print(information_gain(1.0, [[1, 1, 0], [0]]))
    print(information_gain(1.0, [[1, 1], [0, 0]]))


if __name__ == "__main__":
    sys.exit(main())
