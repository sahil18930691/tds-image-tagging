from fastapi import FastAPI, File, UploadFile

from image_tag.predictor import ImagePredictor

app = FastAPI()

predictor_config_path = "config.yaml"

predictor = ImagePredictor.init_from_config_url(predictor_config_path)
@app.get('/')

def index():
    """Sample Function"""
    print(index.__doc__)
    return({'key' : 'value'})

@app.post("/scorefile/")
def create_upload_file(file: UploadFile = File(...)):
    '''This Function is for uploading the file from your device, on which you want to predict'''
    print(create_upload_file.__doc__)
    return predictor.predict_from_file(file.file)
