from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained model
loaded_model = joblib.load('model.joblib')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request JSON
        data = request.get_json(force=True)
        new_email = data['email']

        # Make a prediction using the loaded model
        new_prediction = loaded_model.predict([new_email])

        # Return the prediction as JSON
        response = {'prediction': new_prediction[0]}
        return jsonify(response)

    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
