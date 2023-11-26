# Book Search API

Dataset Used - [Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
This is a simple Flask API that allows you to search for books based on ISBN, Title, and Author. The book data is loaded from a CSV file (`book.csv`).

## Setup

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the API
```
flask run
```

## Endpoints
```
GET /search

Search for books based on the following query parameters:

isbn: ISBN of the book.

title: Title of the book.

author: Author of the book.
```

### Search by ISBN
```
http://127.0.0.1:5000/search?isbn={ISBN}
```

### Search by Title
```
http://127.0.0.1:5000/search?title={Book Title}
```

### Search by Author
```
http://127.0.0.1:5000/search?author={Author}
```

## Response
The API returns a JSON response containing a list of books that match the search criteria. If no books are found, a message is returned.

```
[
  {
    "ISBN": "0195153448",
    "Book-Title": "Classical Mythology",
    "Book-Author": "Mark P. O. Morford",
    "Year-Of-Publication": 2002,
    "Publisher": "Oxford University Press",
    "Image-URL-S": "http://images.amazon.com/images/P/0195153448.01.THUMBZZZ.jpg",
    "Image-URL-M": "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
    "Image-URL-L": "http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg"
  },
  // ... other books ...
]

```

If Empty

```
{
  "message": "No books found for the specified criteria"
}

```
## Project Structure
app.py: The main Flask application file containing the API code.

book.csv: The CSV file containing the book data.

requirements.txt: A file listing the Python packages required for your project. 

## To Contributors 

The book data is loaded from the book.csv file. Make sure this file is present and properly formatted.
The API performs case-insensitive matching for titles and authors.
URL-encode author names to handle special characters properly.

Feel free to enhance this API based on your specific requirements.