from flask import Flask
# from redis import Redis
import os

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

COUNT = 1


@app.route('/')
def hello():
    # redis.incr('hits')
    global COUNT
    COUNT += 1
    return f'Hello World! I have been seen {COUNT} times.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
