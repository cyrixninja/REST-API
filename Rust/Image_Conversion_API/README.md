# Image Conversion API

The Image Conversion API is a simple web service built with Actix-Web and Rust to convert images between different formats. It supports popular image formats such as JPEG, PNG, GIF, and BMP.

## Features

- Convert images from one format to another.
- Supports JPEG, PNG, GIF, and BMP formats.
- Provides a simple HTTP API for image conversion.

## Prerequisites

- Rust programming language and Cargo package manager installed.

## Usage
### Run the API 
Once you're in the current directory run the following commands
```
cargo build --release
cargo run --release
```
### Use the API
1. Send a POST request to `/convert/{format}` where `{format}` is the desired output format (e.g., `jpeg`, `png`, `gif`, or `bmp`).
2. Attach the image data as the request payload.

#### Using cURL:

```
curl -X POST -H "Content-Type: image/jpeg" --data-binary "@path/to/your/image.jpg" http://localhost:8080/convert/png > converted_image.png
```

#### Using Postman:

- Open Postman.
- Create a new request.
-Set the request type to POST.
- Enter the request URL: http://127.0.0.1:8080/convert/{format}, where {format} is the desired output format (e.g., "png", "jpeg", "gif").
- Go to the "Body" tab.
- Select the "Binary" option.
- Choose the image file using the "Select Files" button.
- Click the "Send" button.

![Img](/Rust/Image_Conversion_API/screenshots/1.png)

## Configuration
The API uses a payload limit of 10 MB by default. You can adjust this limit in the main function of main.rs if needed.
