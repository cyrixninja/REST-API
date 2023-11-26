# Email Phishing Classfier using Naive Bayes Classifier

This Flask API provides an endpoint for classifying emails as either phishing or legitimate using a pre-trained machine learning model. The model is loaded using joblib and predicts the classification based on the provided email text. We are using naive bayes algorithm for classification

[Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails)

## Setup

### Install Dependencies
```
pip install -r requirements.txt
```

## Usage

### Run the Flask Server
```
flask run
```

### Make Request using Curl
Send a POST request to the /api/predict endpoint with a JSON payload containing the email to be classified.
```
curl -X POST -H "Content-Type: application/json" -d '{"email":"your_email_text"}' http://127.0.0.1:5000/api/predict
```
Replace "your_email_text" with the actual email text you want to classify.

### Test REST API using Python
```
python test.py
```
### API Response
The API will respond with a JSON object containing the classification
```
{"prediction": "phishing" or "legitimate"}
```
If there are any errors, the API will respond with an error message.

## Project Structure
app.py: Main script containing the Flask application and classification logic.
model.joblib: Pre-trained machine learning model for email phishing classification.
README.md: Documentation for the project.

## Train (Faster Model but Less Accurate)
```
cd Train
```

```
python train1.py
```

## Train (Slower Model but More Accurate)
```
cd Train
```

```
python train2.py
```
## Test 

```
cd Test
```

```
python test.py
```