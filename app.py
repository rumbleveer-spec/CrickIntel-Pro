from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

# Cricket API Configuration
CRICKET_API_KEY = os.getenv('CRICKET_API_KEY', 'your_api_key_here')
CRICKET_API_URL = 'https://api.cricapi.com/v1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/live-matches', methods=['GET'])
def get_live_matches():
    """Fetch live cricket matches"""
    try:
        response = requests.get(f'{CRICKET_API_URL}/currentMatches?apikey={CRICKET_API_KEY}')
        data = response.json()
        return jsonify({'success': True, 'matches': data.get('data', [])})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/match-prediction', methods=['POST'])
def match_prediction():
    """AI-powered match prediction"""
    try:
        match_data = request.json
        # Simple prediction logic (can be enhanced with ML models)
        prediction = {
            'winner': match_data.get('team1', 'Unknown'),
            'confidence': 75,
            'analysis': 'Based on recent form and head-to-head records'
        }
        return jsonify({'success': True, 'prediction': prediction})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/player-stats', methods=['GET'])
def player_stats():
    """Get player statistics"""
    player_id = request.args.get('player_id')
    try:
        response = requests.get(f'{CRICKET_API_URL}/players_info?apikey={CRICKET_API_KEY}&id={player_id}')
        data = response.json()
        return jsonify({'success': True, 'stats': data.get('data', {})})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
