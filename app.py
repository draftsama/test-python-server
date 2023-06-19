from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]


# GET /books - Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/<id> - Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# POST /books - Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        'id': data['id'],
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Run the app
PORT=5000

if __name__ == '__main__':
    #run as https
    app.run(ssl_context='adhoc', host='0.0.0.0', port=PORT)
    #run as http
    # app.run(host='0.0.0.0', port=PORT, debug=True)

    
