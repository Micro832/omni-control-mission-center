from flask import Flask, jsonify, request, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(DATA_DIR, exist_ok=True)

def load_data(filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Initialize sample data
if not os.path.exists(os.path.join(DATA_DIR, 'pipeline.json')):
    save_data('pipeline.json', {
        "leads": [
            {"id": "L001", "name": "Atlantic Healthcare", "company": "AH Systems", "industry": "Healthcare", "roi": "$45K", "status": "Contacted"},
            {"id": "L002", "name": "Camden Legal", "company": "Camden LLP", "industry": "Legal", "roi": "$28K", "status": "Qualified"},
            {"id": "L003", "name": "Jersey Realty", "company": "JR Group", "industry": "Real Estate", "roi": "$18K", "status": "New"}
        ]
    })

if not os.path.exists(os.path.join(DATA_DIR, 'queue.json')):
    save_data('queue.json', {
        "tasks": [
            {"id": "T001", "task": "Generate pitch for Atlantic Healthcare", "cost": "$0.15", "model": "Kimi", "status": "pending"},
            {"id": "T002", "task": "Draft Accounting HW Ch 2", "cost": "$0.08", "model": "MiniMax", "status": "pending"}
        ]
    })

if not os.path.exists(os.path.join(DATA_DIR, 'vitals.json')):
    save_data('vitals.json', {"balance": 47.50, "burn_rate": 3.25, "mode": "Cost Savings", "runway": "14.6 days"})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        'pipeline': load_data('pipeline.json'),
        'queue': load_data('queue.json'),
        'vitals': load_data('vitals.json')
    })

if __name__ == '__main__':
    print('=' * 60)
    print('OMNI-CONTROL MISSION CENTER')
    print('J.A.R.V.I.S. Command Interface')
    print('=' * 60)
    print('Server running on:')
    print('  http://localhost:3000')
    print('  http://192.168.1.185:3000')
    print('=' * 60)
    app.run(host='0.0.0.0', port=3000, debug=False)