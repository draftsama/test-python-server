import os
from flask import Flask, jsonify, request
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

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

cer = '/home/ubuntu/ca-certificates.crt'
key = '/home/ubuntu/ssl-cert-snakeoil.pem'

#check file exists
if not os.path.isfile(cer) or not os.path.isfile(key):
    print("SSL certificate and/or key file not found")
    exit()

if __name__ == '__main__':
    app.run(ssl_context=(cer, key),host='0.0.0.0', port=PORT, debug=True)


    
