from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from src.app.logic.preprocess import preprocess_image
from src.app.api.check_similarity import check_similarity

from PIL import Image

from src.app.logic.preprocess import preprocess_image


stamp_image_path = "src/static/stamp.png"

# スタンプ画像の読み込み
stamp_image = Image.open(stamp_image_path)

# スタンプ画像の前処理
preprocessed_stamp_image = preprocess_image(stamp_image)

# FastAPIアプリケーションの初期化
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# エンドポイントの追加
@app.post("/check_similarity")
async def similarity_endpoint(image_file: UploadFile = File(...)):
    return await check_similarity(preprocessed_stamp_image, image_file)

@app.post("/dojin")
async def dojin(text: str):
    if text == "dojin" or text == "土人" or text == "どじん" or text == "ドジン":
        return { "result": '土人' }
    
@app.get("/dojin")
async def dojin():
    return { "result": '土人' }
