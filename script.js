async function analyzeIdea() {
    const idea = document.getElementById('ideaInput').value;
    const industry = document.getElementById('industrySelect').value;
    
    if (!idea.trim()) {
        alert('Please enter an idea to analyze');
        return;
    }
    
    // Show loading
    const btn = document.getElementById('analyzeBtn');
    btn.innerHTML = 'Analyzing...';
    btn.disabled = true;
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                idea: idea,
                industry: industry
            })
        });
        
        const analysis = await response.json();
        
        // Display results
        displayResults(analysis);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Analysis failed. Please try again.');
    } finally {
        btn.innerHTML = 'Analyze Idea';
        btn.disabled = false;
    }
}

function displayResults(analysis) {
    // Show results section
    document.getElementById('results').classList.remove('hidden');
    
    // Update score
    document.getElementById('scoreValue').textContent = analysis.score;
    
    // Update score circle color based on score
    const scoreCircle = document.querySelector('.score-circle');
    if (analysis.score >= 70) {
        scoreCircle.style.background = 'linear-gradient(135deg, #4CAF50 0%, #45a049 100%)';
    } else if (analysis.score >= 40) {
        scoreCircle.style.background = 'linear-gradient(135deg, #FF9800 0%, #F57C00 100%)';
    } else {
        scoreCircle.style.background = 'linear-gradient(135deg, #F44336 0%, #D32F2F 100%)';
    }
    
    // Update other fields
    document.getElementById('marketSize').textContent = analysis.market_size;
    document.getElementById('competition').textContent = analysis.competition;
    document.getElementById('trends').textContent = analysis.trends;
    
    // Update lists
    updateList('risks', analysis.risks);
    updateList('recommendations', analysis.recommendations);
}

function updateList(elementId, items) {
    const listElement = document.getElementById(elementId);
    listElement.innerHTML = '';
    
    if (Array.isArray(items)) {
        items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            listElement.appendChild(li);
        });
    }
}

// Demo data for testing without backend
function demoAnalyze() {
    const analysis = {
        score: 75,
        market_size: 'Large',
        competition: 'Medium',
        trends: 'AI integration, Remote work solutions',
        risks: ['Market saturation', 'High development costs'],
        recommendations: [
            'Validate with target customers',
            'Create MVP within 3 months',
            'Focus on one core feature first'
        ]
    };
    
    displayResults(analysis);
}