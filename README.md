# XGBoost API

Flask-based API for XGBoost predictions with GPU/CPU support.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python train.py
   ```

3. Run tests:
   ```bash
   pip install -r requirements.txt
   pytest
   ```

4. Run the API:
   ```bash
   python app.py
   ```

## API Endpoints

- `GET /health`: Health check
- `POST /predict`: Make predictions
  - Body: `{"features": [array_of_features]}`
  - Response: `{"prediction": [values], "shape": [dims]}`

## Usage Examples

Health check:
```bash
curl http://localhost:8000/health
```

Prediction:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0, 4.0]}'
```
Response: `{"id":"uuid","prediction":[0.99...],"shape":[1,4]}`

## Requirements

- Python 3.9+ (due to scikit-learn 1.5.0 requirements)
- Optional: NVIDIA GPU with CUDA support
- For GPU: Docker with NVIDIA Container Toolkit, Kubernetes with NVIDIA device plugin

### Mac Setup

Install OpenMP:
```bash
brew install libomp
export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"
```

## Deployment

Docker:
```bash
docker build -t bniladridas/flask-xgboost-api .
docker run --gpus all -p 8000:8000 bniladridas/flask-xgboost-api
```

Test:
1. `docker run -p 8000:8000 bniladridas/flask-xgboost-api`
2. `curl http://localhost:8000/health` → `{"status":"healthy"}`
3. `curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"features": [1.0, 2.0, 3.0, 4.0]}'` → prediction JSON

Kubernetes:
```bash
# Install minikube: https://minikube.sigs.k8s.io/docs/start/
minikube start
kubectl apply -f kubernetes/
```
Requires a Kubernetes cluster (group of nodes for container management).
