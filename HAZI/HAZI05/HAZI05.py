import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix, euclidean_distances

class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self) -> int:
        return self.k
    
    @staticmethod
    def load_csv(path : str):
        dataset = pd.read_csv(path)
    
        dataset = dataset.sample(frac=1, random_state=42)
        
        x = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]
        
        return x, y
    
    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return ((self.X_train - element_of_x)**2).sum(axis=1).apply(lambda x: x**0.5)
    
    def predict(self, x_test):
        labels_pred = []

        for x_test_element in x_test.iterrows():
            distance = self.euclidean(x_test_element)
            distance = pd.DataFrame({'distance': distance, 'label': self.y_train})
            distance = distance.sort_values(by='distance')
            label_pred = distance.head(self.k)['label'].mode().values[0]
            labels_pred.append(label_pred)

        self.y_preds = pd.Series(labels_pred, dtype='int64').values

    def plot_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
    
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def train_set_split(self, features, labels):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!!!"

        x_train, x_test = features.iloc[:-train_size], features.iloc[-train_size:]
        y_train, y_test = labels.iloc[:-train_size], labels.iloc[-train_size:]

        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test