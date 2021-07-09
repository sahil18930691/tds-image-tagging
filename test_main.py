from fastapi.testclient import TestClient
from fastapi import File, UploadFile
from .main import app
from image_tag.predictor import ImagePredictor

predictor_config_path = "config.yaml"

predictor = ImagePredictor.init_from_config_url(predictor_config_path)
client = TestClient(app)
def test_create_upload_file(file: UploadFile = File(...)):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == predictor.predict_from_file(file.file)