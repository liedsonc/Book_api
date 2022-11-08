from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'book 1',
        'autor': 'autor of book 1'
    },
    {
        'id': 2,
        'title': 'book 2',
        'autor': 'autor of book 2'
    },
    {
        'id': 3,
        'title': 'book 3',
        'autor': 'autor of book 3'
    },
]

# Read(all)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Read(id)


@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


# Update


@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            return jsonify(books[index])


# Create


@app.route('/books', methods=['POST'])
def include_new_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

# Delete


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)
