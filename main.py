from fastapi import FastAPI, File, UploadFile
from image_tag.predictor import ImagePredictor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Image Classification",
    description="classify images into different categories")

origins = [
    "https://ai.propvr.tech",
    "http://ai.propvr.tech" 
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


predictor_config_path = "config.yaml"

predictor = ImagePredictor.init_from_config_url(predictor_config_path)
@app.get('/')

def index():
    """Sample Function"""
    print(index.__doc__)
    return({'key' : 'value'})

@app.post("/upload")
def create_upload_file(file: UploadFile = File(...)):
    '''This Function is for uploading the file from your device, on which you want to predict'''
    print(create_upload_file.__doc__)
    return predictor.predict_from_file(file.file)



@app.get("/image_url")
def image_through_url(URL: str):
    '''To Upload Files Through URL'''
    path=URL
    return predictor.predict_from_path(path)
