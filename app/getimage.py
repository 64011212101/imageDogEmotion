from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input
import base64
import io
import tensorflow as tf

def process(uri):
    encoded_data = uri.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    image = Image.open(io.BytesIO(decoded_data))
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    preprocessed_image = preprocess_input(image_array)
    return preprocessed_image

