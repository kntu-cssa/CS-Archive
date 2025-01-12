import numpy as np
import matplotlib.pyplot as plt

# Calculate Gini Impurity for a single node
def gini_impurity_node(y):
    classes, counts = np.unique(y, return_counts=True)
    prob = counts / counts.sum()
    return 1 - np.sum(prob ** 2)

# Calculate Gini Gain for a split
def gini_gain(y, y_left, y_right):
    parent_impurity = gini_impurity_node(y)
    left_impurity = gini_impurity_node(y_left)
    right_impurity = gini_impurity_node(y_right)
    weighted_impurity = # TODO
    return parent_impurity - weighted_impurity

# Split dataset based on a given attribute value
def split(X, y, feature_index, threshold):
    left = X[:, feature_index] <= threshold
    right = X[:, feature_index] > threshold
    return X[left], y[left], X[right], y[right]

class Node:
    def __init__(self, gini, num_samples, num_samples_per_class, predicted_class):
        self.gini = gini
        self.num_samples = num_samples
        self.num_samples_per_class = num_samples_per_class
        self.predicted_class = predicted_class
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None
        self.leaf = True

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.n_classes = len(np.unique(y))
        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y, depth=0):
        num_samples_per_class = [np.sum(y == i) for i in range(self.n_classes)]
        predicted_class = np.argmax(num_samples_per_class)
        node = Node(
            gini=gini_impurity_node(y),
            num_samples=len(y),
            num_samples_per_class=num_samples_per_class,
            predicted_class=predicted_class,
        )
        if depth < self.max_depth and len(set(y)) > 1:
            best_gini_gain = 0
            best_index, best_threshold = None, None
            for feature_index in range(X.shape[1]):
                #TODO: thresholds = 
                for threshold in thresholds:
                    X_left, y_left, X_right, y_right = split(X, y, feature_index, threshold)
                    if len(y_left) > 0 and len(y_right) > 0:
                        gain = gini_gain(y, y_left, y_right)
                        if gain > best_gini_gain:
                            # TODO
            if best_gini_gain > 0:
                node.feature_index = best_index
                node.threshold = best_threshold
                X_left, y_left, X_right, y_right = split(X, y, best_index, best_threshold)
                node.leaf = False
                node.left = self.build_tree(X_left, y_left, depth + 1)
                node.right = self.build_tree(X_right, y_right, depth + 1)
        return node

    def predict(self, X):
        return [self.predict_single_input(inputs) for inputs in X]

    def predict_single_input(self, inputs):
        node = self.tree
        while not node.leaf:
            # TODO
        return node.predicted_class



X = np.array([[2, 3], [1, 1], [2, 1], [5, 3], [5, 6], [4, 4], [6, 6]])
y = np.array([0, 0, 0, 1, 1, 1, 1])
test_points = np.array([[2, 2], [5, 5]])

tree = DecisionTree(max_depth=3)
tree.fit(X, y)
print(tree.predict(test_points)) 

