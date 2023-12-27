from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test', methods=['POST'])
def test():
    text = request.form['text']
    return f"Message received: {text}"


if __name__ == '__main__':
    app.run()
