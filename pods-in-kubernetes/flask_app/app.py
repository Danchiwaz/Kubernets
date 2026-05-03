import  logging
import time

from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
start_time = time.time()


@app.route('/')
def hello():
    logger.info("Processing request for '/' endpoint")
    return 'Hello from kubernetes, becoming the best devops engineer there can ever be'

@app.route('/health')
def health():
    # Fails for the first 30s and then it recovers
    elapsed_time = time.time() - start_time
    if elapsed_time < 30 :
        return "unhealth", 500
    return "Ok", 200

if __name__ == '__main__':
    time.sleep(5) #simulating slow start -up
    app.run(debug=True, host='0.0.0.0', port=6000)
