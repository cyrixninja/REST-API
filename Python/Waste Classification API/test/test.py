import requests


url = "http://127.0.0.1:5000/classify"

# Test Organic
files = {'image': ('image.jpg', open('image.jpg', 'rb'))}

response = requests.post(url, files=files)

print(response.json())

# Test Recyclable
files = {'image': ('image2.jpg', open('image2.jpg', 'rb'))}

response = requests.post(url, files=files)

print(response.json())