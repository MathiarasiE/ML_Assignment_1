import pandas as pd
import math

def entropy(data):
    total = len(data)
    counts = data['Buys'].value_counts()

    ent = 0
    for c in counts:
        p = c/total
        ent -= p * math.log2(p)
    return ent

def information_gain(data, attribute):
    total_entropy = entropy(data)

    values = data[attribute].unique()
    weighted_entropy = 0

    for v in values:
        subset = data[data[attribute] == v]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset)

    return total_entropy - weighted_entropy

def id3(data, attributes):
    if len(data['Buys'].unique()) == 1:
        return data['Buys'].iloc[0]

    if not attributes:
        return data['Buys'].mode()[0]

    gains = {attr: information_gain(data, attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)

    tree = {best_attr: {}}

    for v in data[best_attr].unique():
        subset = data[data[best_attr] == v]
        subtree = id3(subset, [a for a in attributes if a != best_attr])
        tree[best_attr][v] = subtree

    return tree

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    attr = next(iter(tree))
    value = sample[attr]

    return predict(tree[attr][value], sample)
