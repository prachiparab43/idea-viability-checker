from flask import Flask, render_template, request, jsonify
from analyzer import analyze_idea
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        idea = data.get('idea', '').strip()
        industry = data.get('industry', 'Technology')
        
        if not idea:
            return jsonify({'error': 'Please enter an idea'})
        
        if len(idea) > 1000:
            return jsonify({'error': 'Idea too long (max 1000 chars)'})
        
        analysis = analyze_idea(idea, industry)
        analysis['success'] = True
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({
            'error': 'Analysis failed. Try again.',
            'success': False
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
