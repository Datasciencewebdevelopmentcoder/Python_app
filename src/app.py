from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little humans people! hello by the way!! 3 test mod',
        'deployed_on': 'kubernetes, multi-image type test or go back to v2'
        
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200


if __name__ == '__main__':

    app.run(host="0.0.0.0")
