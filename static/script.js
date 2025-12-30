async function analyzeIdea() {
    const idea = document.getElementById('ideaInput').value.trim();
    const industry = document.getElementById('industrySelect').value;
    
    if (!idea) {
        alert('Please enter your startup idea');
        return;
    }
    
    const btn = document.getElementById('analyzeBtn');
    btn.innerHTML = 'Analyzing...';
    btn.disabled = true;
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ idea, industry })
        });
        
        const analysis = await response.json();
        
        if (analysis.success) {
            displayResults(analysis);
        } else {
            alert(analysis.error || 'Analysis failed');
        }
        
    } catch (error) {
        alert('Network error. Please try again.');
    } finally {
        btn.innerHTML = 'Analyze Idea';
        btn.disabled = false;
    }
}

function displayResults(analysis) {
    document.getElementById('results').style.display = 'block';
    document.getElementById('scoreValue').textContent = analysis.score;
    document.getElementById('marketSize').textContent = analysis.market_size;
    document.getElementById('competition').textContent = analysis.competition;
    document.getElementById('trends').textContent = analysis.trends;
    
    // Update lists
    updateList('recommendations', analysis.recommendations);
    updateList('risks', analysis.risks);
}

function updateList(elementId, items) {
    const ul = document.getElementById(elementId);
    ul.innerHTML = '';
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        ul.appendChild(li);
    });
}
