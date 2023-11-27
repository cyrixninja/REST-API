from flask import Flask, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2
import os

app = Flask(__name__)

static_dir = "api/static/"
os.makedirs(static_dir, exist_ok=True)

# Load the Model
model = load_model("waste_classification_model.h5")

# Class Labels
class_labels = ["Organic", "Recyclable"]

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0  # Normalize pixel values
    img = np.reshape(img, (1, 224, 224, 3))
    return img

@app.route('/classify', methods=['POST'])
def classify_waste():
    try:
        # Get the image file from the request
        file = request.files['image']
        file_path = os.path.join(static_dir, "temp_image.jpg")
        file.save(file_path)

        # Preprocess the image
        img = preprocess_image(file_path)

        # Make predictions
        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions)
        predicted_class = class_labels[predicted_class_index]

        response = {'result': predicted_class}
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
