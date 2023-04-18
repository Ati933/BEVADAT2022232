import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        iris = load_iris()
        self.epochs = epochs
        self.df = pd.DataFrame(iris.data, columns=iris.feature_names)

        self.df['target'] = iris.target

    def fit(self, X: np.array, y: np.array):
        X_train, self.X_test, y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Building the model
        self.m = 0
        self.c = 0

        L = 0.0001  # The learning Rate
        #epochs = 1000  # The number of iterations to perform gradient descent

        n = float(len(X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m * X_train + self.c  # The current predicted value of Y

            residuals = y_pred - y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + L * D_m  # Update m
            self.c = self.c + L * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(y_train - y_pred))

    def predict(self, X):
        y_pred = self.m * X + self.c

        plt.scatter(X, self.y_test)
        plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red') # predicted
        plt.show()
