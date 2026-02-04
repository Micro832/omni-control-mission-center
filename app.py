from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        'status': 'ok',
        'message': 'Mission Control Center is running'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))