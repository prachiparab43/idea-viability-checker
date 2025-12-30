from flask import Flask, render_template, request, jsonify
from analyzer import analyze_idea
import sqlite3
from datetime import datetime
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Analyze idea endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    idea = data.get('idea', '')
    industry = data.get('industry', 'Technology')
    
    if not idea:
        return jsonify({'error': 'Please enter an idea'})
    
    # Get AI analysis
    analysis = analyze_idea(idea, industry)
    
    # Save to database (optional - Vercel has ephemeral storage)
    # save_analysis(idea, analysis)
    
    return jsonify(analysis)

# Static file serving
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Add this for Vercel
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

# Remove the app.run() line or modify it
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)