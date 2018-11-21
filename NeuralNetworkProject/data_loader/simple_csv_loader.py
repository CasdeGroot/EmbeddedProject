from base.base_data_loader import BaseDataLoader
from sklearn.model_selection import train_test_split
import pandas as pd


class SimpleCSVLoader(BaseDataLoader):
    def __init__(self, config):
        super(SimpleCSVLoader, self).__init__(config)
        df = pd.read_csv(config.dataset)



    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test