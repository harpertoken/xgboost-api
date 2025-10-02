from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np
import os
import uuid

app = Flask(__name__)

# Load model at startup
model_path = os.path.join('model', 'xgboost_model.json')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}. Please run 'python train.py' to train the model first.")
model = xgb.Booster()
model.load_model(model_path)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from request
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
            
        # Convert to DMatrix
        features = np.array(data['features'])
        if len(features.shape) == 1:
            features = features.reshape(1, -1)
            
        dmatrix = xgb.DMatrix(features)
        
        # Make prediction
        prediction = model.predict(dmatrix)
        
        return jsonify({
            'id': str(uuid.uuid4()),
            'prediction': prediction.tolist(),
            'shape': features.shape
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/version', methods=['GET'])
def version():
    return jsonify({'version': '1.0.0'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
