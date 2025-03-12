# XGBoost API

A Flask-based API serving XGBoost predictions with GPU support.

## Version

Current version: 1.0.0 (see [CHANGELOG.md](CHANGELOG.md) for details)

## Project Structure
```
xgboost-api/
├── app.py              # Flask application
├── train.py           # Model training script
├── requirements.txt   # Python dependencies
├── Dockerfile        # Container configuration
├── model/           # Directory for model files
├── kubernetes/      # Kubernetes configurations
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

## Setup and Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the model:
```bash
python train.py
```

4. Build and run Docker container:
```bash
docker build -t bniladridas/flask-xgboost-api .
docker run --gpus all -p 5000:5000 bniladridas/flask-xgboost-api
```

5. Deploy to Kubernetes:
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

## API Endpoints

- `GET /health`: Health check endpoint
- `POST /predict`: Make predictions
  - Request body: `{"features": [array_of_features]}`
  - Response: `{"prediction": [prediction_values]}`

## Requirements

- Python 3.8+
- NVIDIA GPU with CUDA support
- Docker with NVIDIA Container Toolkit
- Kubernetes cluster with NVIDIA device plugin

## Releases

For information about releases and versioning:

- See [CHANGELOG.md](CHANGELOG.md) for version history
- See [RELEASE.md](RELEASE.md) for release process
- Check [GitHub Releases](https://github.com/your-username/xgboost-api/releases) for official releases

To create a new release:
```bash
python scripts/release.py --version X.Y.Z
```
