import pytest
from models.model import eval_model

def test_eval_model(trained_model, data):
    X_test, y_test = data
    accuracy, loss = eval_model(trained_model, X_test, y_test)
    assert accuracy >= 0 and accuracy <= 1
    assert loss >= 0
