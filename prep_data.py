import os

import numpy as np
import pandas as pd
import sklearn
import logging
from sklearn.preprocessing import RobustScaler
from zlib import crc32

from log_decorators import exception_, time_
from create_logger import create_logger, logger

def _load_data(filename):
    return pd.read_csv('sunspots.csv')


def _split_train_test_on_time(data, test_ratio, var):
    train_ratio = 1 - test_ratio
    months = data[var]
    split_point = int(round(len(months) * train_ratio))
    in_test_set = months[split_point:].index
    in_train_set = months[:split_point].index
    return data.loc[in_train_set], data.loc[in_test_set]


@time_(logger)
def prep_data(filename, data):
    data_with_id = data.reset_index()
    train_set, test_set = _split_train_test_on_time(data_with_id, 0.2, 'Month')
    return train_set, test_set


if __name__ == '__main__':
    logger = create_logger()
    filename = 'sunspots.csv'
    data = _load_data(filename)
    train_set, test_set = prep_data(filename, data)
    logger.info('\n {}'.format(train_set.head()))
