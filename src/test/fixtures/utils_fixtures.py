import pytest
import os

from models.model import load_data, train_model

@pytest.fixture
def data():
    """
    Load data for the model
    """
    actual_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = actual_path.replace('/test/fixtures', '')
    filepath_ = os.path.join(data_folder, 'data', 'heart_disease_uci.csv')
    #filepath_ = os.path.join(data_folder, 'data', 'clean_strings_heart_disease_uci.csv')
    #filepath_ = os.path.join(data_folder, 'data', 'clean_nulls_heart_disease_uci.csv')
    X, y = load_data(filepath_)
    return X, y


@pytest.fixture
def trained_model(data):
    """
    Trained model
    """
    X, y = data
    params = {'n_estimators': [10, 50, 100], 'max_depth': [None, 10, 20]}
    model = train_model(X, y, params)
    return model

