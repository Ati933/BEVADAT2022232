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
    def load_csv(path : str) -> Tuple[pd.core.frame.DataFrame, pd.core.series.Series]:
        dataset = pd.read_csv(path)
    
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        
        x = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]
        
        return x, y
    
    def euclidean(self, element_of_x: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
        return ((self.X_train - element_of_x)**2).sum(axis=1).apply(lambda x: x**0.5)
    
    def predict(self, x_test):
        labels_pred = []

        for x_test_element in x_test.iterrows():
            distance = self.euclidean(x_test_element)
            distance = pd.DataFrame(sorted(zip(distance, self.y_train)))
            
            label_pred = distance.iloc[:self.k, 1].mode()
            labels_pred.append(label_pred)

        self.y_preds = pd.DataFrame(labels_pred).iloc[:, 0]

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
    
    def accuracy(self) -> float:
        true_positive = (self.y_test.reset_index(drop=True) == self.y_preds.reset_index(drop=True)).sum()
        return true_positive / len(self.y_test) * 100
    
    def train_test_split(self, features, labels):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!!"

        x_train, x_test = features.iloc[:train_size, :], features.iloc[train_size:train_size+test_size, :]
        y_train, y_test = labels.iloc[:train_size], labels.iloc[train_size:train_size+test_size]

        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def best_accuracy(self) -> Tuple[int, float]:
        best_k = -1
        max_acc = -1

        for i in range(1, 21):
            self.k = i
            self.predict(self, self.x_test)
            pred_acc = self.accuracy(self)

            if (pred_acc > max_acc):
                best_k = self.k
                max_acc = pred_acc

        return int(best_k), float(round(max_acc, 2))