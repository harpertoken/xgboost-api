import numpy as np
import xgboost as xgb
import os
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def create_sample_data():
    # Generate a random dataset for demonstration
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    # Create sample data
    X_train, X_test, y_train, y_test = create_sample_data()
    
    # Convert to DMatrix format
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)
    
    # Set parameters
    params = {
        'max_depth': 6,
        'eta': 0.3,
        'objective': 'binary:logistic',
        'eval_metric': 'logloss',
        'tree_method': 'hist'  # Use CPU for compatibility
    }
    
    # Train model
    num_rounds = 100
    model = xgb.train(params, dtrain, num_rounds)

    # Ensure model directory exists
    os.makedirs('model', exist_ok=True)

    # Save model
    model.save_model('model/xgboost_model.json')
    print("Model saved successfully!")

if __name__ == "__main__":
    train_model()
