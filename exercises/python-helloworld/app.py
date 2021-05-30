from logging.config import dictConfig
import logging

from flask import Flask, json, request

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s.%(msecs)03d [%(levelname).3s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'console': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10,
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    }
})

# set log level for flasks default logger
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)


@app.route("/status")
def healthcheck():
    app.logger.info(f'{request.path} endpoint was reached')
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/metrics")
def metrics():
    app.logger.info(f'{request.path} endpoint was reached')
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/")
def hello():
    app.logger.info(f'{request.path} endpoint was reached')
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
