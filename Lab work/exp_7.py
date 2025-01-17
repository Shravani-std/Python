

import numpy as np
from collections import Counter

# Calculate entropy
def entropy(y):
    """Compute the entropy of a label array."""
    counts = Counter(y)
    total = len(y)
    entropy_value = 0
    for count in counts.values():
        prob = count / total
        entropy_value -= prob * np.log2(prob) if prob > 0 else 0
    return entropy_value

# Calculate information gain
def information_gain(X, y, feature_index):
    """Calculate the information gain of a feature (column) in the dataset."""
    total_entropy = entropy(y)
    feature_values = set(X[:, feature_index])
    weighted_entropy = 0

    for value in feature_values:
        subset_y = y[X[:, feature_index] == value]
        weighted_entropy += len(subset_y) / len(y) * entropy(subset_y)

    return total_entropy - weighted_entropy

# Find the best feature to split on
def best_split(X, y):
    """Find the feature that gives the highest information gain."""
    best_gain = 0
    best_feature = None
    for feature_index in range(X.shape[1]):
        gain = information_gain(X, y, feature_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    return best_feature

# Build the decision tree
def build_tree(X, y):
    """Recursively build a decision tree."""
    if len(set(y)) == 1:  # If all labels are the same, return a leaf node
        return {'label': y[0]}

    if X.shape[1] == 0:  # If no features left to split on, return the most common label
        most_common_label = Counter(y).most_common(1)[0][0]
        return {'label': most_common_label}

# Find the best feature to split on
best_feature = best_split(X, y)

    if best_feature is None:
        most_common_label = Counter(y).most_common(1)[0][0]
        return {'label': most_common_label}

    tree = {'feature': best_feature, 'branches': {}}

# Split the dataset based on the best feature
feature_values = set(X[:, best_feature])
    for value in feature_values:
        subset_X = X[X[:, best_feature] == value]
        subset_y = y[X[:, best_feature] == value]
        tree['branches'][value] = build_tree(subset_X, subset_y)

    return tree

Let's build a simple classification algorithm using Entropy and Information Gain. We'll use a small dataset and build a decision tree based on those concepts.

Problem Overview
We will use a small dataset where the task is to predict whether a customer will buy a product (1 for buy, 0 for not buy) based on two features:

Age (e.g., 0 for Young, 1 for Old)
Income (e.g., 0 for Low, 1 for High)
Data Example
Age	Income	Buy
0	0	0
0	1	1
1	0	0
1	1	1
We will use entropy to measure the impurity of a dataset and information gain to decide which feature to split on in our decision tree.

Step-by-Step Implementation
Here’s a simple implementation of a decision tree classifier using entropy and information gain.

python
Copy code
import numpy as np
from collections import Counter

# Calculate entropy
def entropy(y):
    """Compute the entropy of a label array."""
    counts = Counter(y)
    total = len(y)
    entropy_value = 0
    for count in counts.values():
        prob = count / total
        entropy_value -= prob * np.log2(prob) if prob > 0 else 0
    return entropy_value

# Calculate information gain
def information_gain(X, y, feature_index):
    """Calculate the information gain of a feature (column) in the dataset."""
    total_entropy = entropy(y)
    feature_values = set(X[:, feature_index])
    weighted_entropy = 0

    for value in feature_values:
        subset_y = y[X[:, feature_index] == value]
        weighted_entropy += len(subset_y) / len(y) * entropy(subset_y)

    return total_entropy - weighted_entropy

# Find the best feature to split on
def best_split(X, y):
    """Find the feature that gives the highest information gain."""
    best_gain = 0
    best_feature = None
    for feature_index in range(X.shape[1]):
        gain = information_gain(X, y, feature_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    return best_feature

# Build the decision tree
def build_tree(X, y):
    """Recursively build a decision tree."""
    if len(set(y)) == 1:  # If all labels are the same, return a leaf node
        return {'label': y[0]}

    if X.shape[1] == 0:  # If no features left to split on, return the most common label
        most_common_label = Counter(y).most_common(1)[0][0]
        return {'label': most_common_label}

    # Find the best feature to split on
    best_feature = best_split(X, y)

    if best_feature is None:
        most_common_label = Counter(y).most_common(1)[0][0]
        return {'label': most_common_label}

    tree = {'feature': best_feature, 'branches': {}}

    # Split the dataset based on the best feature
    feature_values = set(X[:, best_feature])
    for value in feature_values:
        subset_X = X[X[:, best_feature] == value]
        subset_y = y[X[:, best_feature] == value]
        tree['branches'][value] = build_tree(subset_X, subset_y)

    return tree

# Predict a single example
def predict_one(tree, x):
    """Make a prediction for a single sample."""
    if 'label' in tree:
        return tree['label']

    feature_value = x[tree['feature']]
    return predict_one(tree['branches'][feature_value], x)

# Predict for multiple samples
def predict(tree, X):
    """Make predictions for multiple samples."""
    return [predict_one(tree, x) for x in X]

# Example usage
if __name__ == "__main__":
    # Example dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # [Age, Income]
    y = np.array([0, 1, 0, 1])  # Buy (0 = No, 1 = Yes)

    # Build decision tree
    tree = build_tree(X, y)
    print("Decision Tree:", tree)

    # Test the tree with predictions
    test_data = np.array([[0, 1], [1, 0]])  # Test with new samples
    predictions = predict(tree, test_data)
    print("Predictions for test data:", predictions)