import os

def analyze_idea(idea, industry):
    """Analyze startup idea with rule-based system"""
    
    # Calculate score
    score = 50
    
    # Industry bonus
    hot_industries = ['Technology', 'AI', 'Healthcare', 'Fintech']
    if industry in hot_industries:
        score += 15
    
    # Idea quality
    if len(idea.split()) > 10:
        score += 10
    
    problem_keywords = ['solve', 'help', 'improve', 'reduce', 'automate']
    if any(word in idea.lower() for word in problem_keywords):
        score += 20
    
    score = min(score, 100)
    
    # Market size
    market_sizes = {
        'Technology': 'Large',
        'Healthcare': 'Very Large',
        'Education': 'Large',
        'Finance': 'Large',
        'AI': 'Very Large',
        'Other': 'Medium'
    }
    market_size = market_sizes.get(industry, 'Medium')
    
    # Competition
    competitive_keywords = ['app', 'platform', 'marketplace', 'social']
    if any(word in idea.lower() for word in competitive_keywords):
        competition = 'High'
    else:
        competition = 'Medium'
    
    # Recommendations
    recommendations = [
        "Validate with target customers first",
        "Build MVP in 3 months",
        "Focus on one core feature",
        "Research 3 competitors"
    ]
    
    # Risks
    risks = [
        "Market competition",
        "User acquisition cost",
        "Technical complexity"
    ]
    
    # Trends
    trends = {
        'Technology': 'AI integration, Remote solutions',
        'Healthcare': 'Telemedicine, Health tech',
        'Education': 'Online learning, EdTech',
        'Finance': 'FinTech, Digital banking'
    }
    
    return {
        'score': score,
        'market_size': market_size,
        'competition': competition,
        'trends': trends.get(industry, 'Digital transformation'),
        'recommendations': recommendations,
        'risks': risks,
        'idea_preview': idea[:100] + '...' if len(idea) > 100 else idea
    }
