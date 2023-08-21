import io
from PIL import Image
from fastapi import File, UploadFile
from src.app.logic.extract import extract_features
from src.app.logic.preprocess import preprocess_image
from src.app.logic.calculate_similarity import calculate_similarity

async def check_similarity(stamp_image: Image.Image, file: UploadFile = File(...)):
    image_contents = await file.read()
    
    image_byte = io.BytesIO(image_contents)

    image = Image.open(image_byte)
    
    preprocessed_image = preprocess_image(image)

    features_image = extract_features(preprocessed_image)

    features_stamp = extract_features(stamp_image)
    
    similarity = calculate_similarity(features_image, features_stamp)

    # TODO: 閾値は調整できるようにする
    if similarity < 130:
        result = "これは土人です。"
    else:
        result = "これは土人ではありません。"

    return { "result": result, "similarity": similarity }
