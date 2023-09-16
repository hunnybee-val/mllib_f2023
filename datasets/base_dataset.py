import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
from configs.linear_regression_dataset import cfg  


class BaseDataset(ABC):

    def __init__(self,train_set_percent,valid_set_percent):
        self.train_set_percent = train_set_percent
        self.valid_set_percent = valid_set_percent

    @property
    @abstractmethod
    def targets(self):
        # targets variables
        pass

    @property
    @abstractmethod
    def inputs(self):
        # inputs variables
        pass


    def _divide_into_sets(self):
        # TODO define self.inputs_train, self.targets_train, self.inputs_valid, self.targets_valid,
        #  self.inputs_test, self.targets_test
        df = pd.read_csv()
        columns = ['inputs','targets']
        df = df.loc[:, columns]
         pass
