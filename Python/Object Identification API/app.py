from flask import Flask, request, jsonify
from PIL import Image
import io
from ultralytics import YOLO

app = Flask(__name__)

# Load the YOLO model
model = YOLO('yolov8m.pt')

# Define the route for object detection
@app.route('/identify_objects', methods=['POST'])
def identify_objects():
    try:
        # Read the binary data from the request body
        image_binary = request.get_data()

        # Convert the binary data to PIL Image
        image = Image.open(io.BytesIO(image_binary))

        # Perform object detection
        results = model([image])

        # Process the results and extract object information
        object_list = []
        for result in results:
            for box in result.boxes:
                class_id = result.names[box.cls[0].item()]
                cords = [round(x) for x in box.xyxy[0].tolist()]
                conf = round(box.conf[0].item(), 2)

                # Create a dictionary for each detected object
                object_info = {
                    "class": class_id,
                    "coordinates": cords,
                    "probability": conf
                }

                object_list.append(object_info)

        # Return the list of detected objects
        return jsonify({"results": object_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
