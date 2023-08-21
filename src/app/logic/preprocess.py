from PIL import Image

def preprocess_image(image: Image.Image, size=(256, 256)) -> Image.Image:
    image_resized = image.resize(size)

    return image_resized

def ensure_rgba(image: Image.Image) -> Image.Image:
    if image.mode != 'RGBA':
        return image.convert('RGBA')
    return image