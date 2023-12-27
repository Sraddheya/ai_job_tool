from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/submit_cv', methods=['POST'])
def submit_cv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Process the file as needed (e.g., save it to a folder, perform operations, etc.)
    # For example, you can save the file to the 'uploads' folder
    file.save('uploads/' + file.filename)

    return jsonify({'message': 'File uploaded successfully'})


if __name__ == '__main__':
    app.run()
