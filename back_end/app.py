from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/submit_cv', methods=['POST'])
def upload_file():
    uploaded_file = request.files['cv']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run()
