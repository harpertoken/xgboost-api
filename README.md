<p align="center">
  <img src="https://raw.githubusercontent.com/Coccinella-Labs/xgboostapi/main/.github/assets/thumbnail.png" alt="xgboostapi" width="100%">
</p>

flask service for xgboost predictions.

Flask API serving a trained XGBoost model from `model/xgboost_model.json` (run `python train.py` first if the model file is missing).

## Endpoints

- `GET /health` - returns `{"status": "healthy"}`
- `POST /predict` - accepts `{"features": [...]}` (1D or 2D array), returns an id, prediction values, and input shape. Returns 400 when features are missing or invalid.

```bash
curl -X POST localhost:5000/predict \
  -H 'Content-Type: application/json' \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## Run

```bash
pip install -r requirements.txt
python app.py
```

Docker and Kubernetes manifests are included (`Dockerfile`, `kubernetes/`).

## Layout

- `app.py` - Flask service (`/health`, `/predict`)
- `train.py` - model training
- `tests/test_app.py` - service tests
- `scripts/` - release helpers
