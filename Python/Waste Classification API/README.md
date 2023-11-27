# Waste Classification API using a Convolutional Neural Network (CNN) Model

This project provides a REST API for classifying waste images into organic and recyclable categories using a Convolutional Neural Network (CNN) model.

[Dataset](https://www.kaggle.com/datasets/techsash/waste-classification-data)

## Setup

Install Dependencies 
```
pip install -r requirements.txt
```

## Usage 

### Run the Flask Server
```
flask run
```

### Make Request using Curl

```
curl -X POST -F "image=@/path/to/your/image.jpg" http://localhost:5000/classify
```
Replace /path/to/your/image.jpg with the actual path to the image file you want to classify.

### Test REST API using Python

Make sure Open new Terminal to Test the REST API.

```
cd test

python test.py
```


### API Response
The API will respond with a JSON object containing the classification
```
{"result": "Recyclable" or "Organic"}
```
If there are any errors, the API will respond with an error message.

## Project Structure
app.py: Main Flask application script.
waste_classification_model.h5: Pre-trained CNN model file.
api/static/: Directory to store temporary image files.
/train/train.py : Script to Train the Model
/test/test.py : Script to Test the Model


## Train the Model (Optional)
This step is only required if you want to change the model.

Download the [Dataset](https://www.kaggle.com/datasets/techsash/waste-classification-data) and place it in /train directory before proceeding to this step.

Structure should look like this before proceeding
```
Structure :

/DATASET
train.py
waste_classification_model.h5
```

```
cd train
python train.py
```