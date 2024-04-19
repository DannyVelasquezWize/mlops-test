# src/modelo_salud.py
import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss
from joblib import dump, load

def load_data(filename_:str) -> Tuple[pd.DataFrame, pd.Series]:
    data = pd.read_csv(filename_)
    X = data.drop('num', axis=1)
    y = data['num']
    
    return X, y


def train_model(X, y, params, size=0.2, randstate=42, cv_=5, scoring_='neg_log_loss'):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size, random_state=randstate)
    
    model = RandomForestClassifier(random_state=randstate)
    
    # hyperparameters
    param_grid = {
        'n_estimators': params['n_estimators'],
        'max_depth': params['max_depth']
    }
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv_, scoring=scoring_, error_score='raise')
    grid_search.fit(X_train, y_train)
    
    model = grid_search.best_estimator_
    
    dump(model, 'trained_model.joblib')
    
    # return model, X_test, y_test
    return model

def eval_model(model, X_test, y_test):
    # Predict
    y_pred = model.predict(X_test)
    
    # 1 attribute
    accuracy = accuracy_score(y_test, y_pred)
    
    # Binary Cross Entropy
    loss = log_loss(y_test, model.predict_proba(X_test))
    
    return accuracy, loss
