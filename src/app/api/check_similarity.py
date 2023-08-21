import io
from PIL import Image
from fastapi import File, UploadFile
from src.app.logic.extract import extract_features
from src.app.logic.preprocess import preprocess_image
from src.app.logic.calculate_similarity import calculate_similarity

async def check_similarity(stamp_image: Image.Image, file: UploadFile = File(...)):
    # 投稿された画像を読み込む
    image_contents = await file.read()
    
    image_byte = io.BytesIO(image_contents)

    image = Image.open(image_byte)
    # 画像の前処理
    preprocessed_image = preprocess_image(image)

    # 特徴抽出
    features_image = extract_features(preprocessed_image)

    # スタンプ画像の特徴抽出
    features_stamp = extract_features(stamp_image)
    
    # 類似度計算
    similarity = calculate_similarity(features_image, features_stamp)

    # 類似度が閾値以上か判定（閾値は調整）
    if similarity < 130:
        result = "これは土人です。"
    else:
        result = "これは土人ではありません。"

    return { "result": result, "similarity": similarity }
