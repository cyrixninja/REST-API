from flask import Flask, jsonify, request
import pandas as pd
import urllib.parse

app = Flask(__name__)

# Load the book data from the CSV file
book_data = pd.read_csv('books.csv')

@app.route('/search', methods=['GET'])
def search_books():
    # Get the search parameters from the query string
    isbn = request.args.get('isbn')
    title = request.args.get('title')
    author = urllib.parse.unquote(request.args.get('author', ''))

    # Filter the book data based on the search parameters
    filtered_books = book_data
    if isbn:
        filtered_books = filtered_books[filtered_books['ISBN'] == isbn]
    if title:
        filtered_books = filtered_books[filtered_books['Book-Title'].str.contains(title, case=False)]
    if author:
        # Use case-insensitive matching for author names
        filtered_books = filtered_books[filtered_books['Book-Author'].str.lower().str.contains(author.lower(), na=False)]

    # Convert the filtered data to JSON and return it
    result = filtered_books.to_dict(orient='records')

    # Check if any books were found
    if not result:
        return jsonify({'message': 'No books found for the specified criteria'})

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
