from flask import Flask

app: Flask = Flask(__name__)


@app.route('/')
def homepage() -> str:
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
