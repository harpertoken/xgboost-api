# XGBoost API

A Flask-based API serving XGBoost predictions with GPU support.

## Project Description

This project provides an API service for XGBoost predictions with GPU support. It includes a Flask-based API with endpoints for health check and prediction, Docker containerization, and Kubernetes deployment configurations. The model training script is also included.

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

## Using the API

### Health Check Endpoint

**Request:**
```bash
curl -X GET http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### Prediction Endpoint

**Request:**
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [1.0, 2.0, 3.0, 4.0]}'
```

**Response:**
```json
{
  "prediction": [0.123456789],
  "shape": [1, 4]
}
```

## Contributing

We welcome contributions to the project! Here are some ways you can contribute:

1. **Report Bugs**: If you find a bug, please report it by opening an issue on GitHub.
2. **Suggest Features**: If you have an idea for a new feature, please suggest it by opening an issue on GitHub.
3. **Submit Pull Requests**: If you want to contribute code, please fork the repository and submit a pull request with your changes.

Please make sure to follow the project's coding standards and write tests for your changes.

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
