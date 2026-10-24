from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "model_loaded": True,
    }


def test_prediction_with_valid_features():
    response = client.post(
        "/predict",
        json={"features": [0.0] * 30},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["prediction"] in [0, 1]
    assert data["predicted_class"] in ["malignant", "benign"]


def test_prediction_with_too_few_features():
    response = client.post(
        "/predict",
        json={"features": [0.0, 0.0, 0.0]},
    )

    assert response.status_code == 422


def test_prediction_with_non_numeric_feature():
    features = [0.0] * 30
    features[0] = "invalid"

    response = client.post(
        "/predict",
        json={"features": features},
    )

    assert response.status_code == 422
