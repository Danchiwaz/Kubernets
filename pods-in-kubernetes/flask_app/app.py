import  logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()


@app.route('/')
def hello():
    logger.info("Processing request for '/' endpoint")
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
