

from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/details')

def details():
    return jsonify({
        'message': 'Sample Flask Application',
        'version': '1.0.0',
        'description': 'This is a sample Flask application for demonstration purposes.'
    })

@app.route('/api/v1/healthz')


def health():
    return jsonify({
        'status': 'Sample Flask Application up and running',
        'timestamp': datetime.datetime.now().strftime("%I: %M%p %S") + 'Z',
        'hostname': socket.gethostname()
    }), 200


if __name__ == '__main__':


    app.run(host='0.0.0.0')

