# Example script to train and save CatBoost model

from catboost import CatBoostRegressor
import pickle

# Assume X_train, y_train are defined from your dataset

# Initialize CatBoostRegressor
cb_model = CatBoostRegressor()

# Fit the model
cb_model.fit(X_train, y_train)

# Save the model to a file
model_file = 'catboost_model.pkl'
with open(model_file, 'wb') as f:
    pickle.dump(cb_model, f)

print(f"Model saved as {model_file}")
