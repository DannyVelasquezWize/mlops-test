import pytest
import os
import pandas as pd

from models.model import load_data

def test_load_data():
    actual_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = actual_path.replace('/test/artifacts', '')
    filepath_ = os.path.join(data_folder, 'data', 'heart_disease_uci.csv')
    var1, var2 = load_data(filepath_)
    assert type(var1) == pd.DataFrame
    assert type(var2) == pd.Series
    assert 'num' in var1.columns
