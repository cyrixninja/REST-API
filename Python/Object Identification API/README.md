# Object Identification API

This API provides a simple and efficient way to perform object identification using YOLOv8 models. Given an input image, the API identifies objects present in the image, providing information such as class, coordinates, and probability.


## Getting Started

- [Ultralytics](https://docs.ultralytics.com/) 

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/cyrixninja/REST-API-Library

    cd Python

    cd 'Object Identification API'
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the API:

    ```
    flask run
    ```

The API will be accessible at `http://localhost:5000`

## API Endpoints

### Identify Objects

- **Endpoint**: `/identify_objects`
- **Method**: POST
- **Parameters**:
  - `image` (binary): Image file for object identification.

#### Example Usage using cURL

```
curl -X POST -H "Content-Type: image/jpeg" --data-binary "@images/img.jpg" http://localhost:5000/identify_objects
```
#### Example Usage using Postman
##### Identify Objects
- Endpoint: http://localhost:5000/identify_objects
- Method: POST
- Headers:
    - Content-Type: image/jpeg
- Body: Select the binary file option and upload an image file (e.g., img.jpg)

![Img](/screenshots/1.png)


### Example Response 
The API will return a JSON response with identified objects
```
{
  {
    "results": [
        {
            "class": "cat",
            "coordinates": [
                198,
                35,
                1174,
                835
            ],
            "probability": 0.93
        },
        {
            "class": "bed",
            "coordinates": [
                18,
                234,
                1192,
                888
            ],
            "probability": 0.43
        }
    ]
}

```