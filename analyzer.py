import requests
import json

# Using free Hugging Face inference API
# Sign up at huggingface.co for free API token

HUGGINGFACE_API_KEY = "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"  # Replace with your key

def analyze_idea(idea, industry):
    """
    Analyze idea using AI models
    """
    
    # Simple rule-based scoring as fallback
    # Replace with actual API calls
    
    analysis = {
        'score': calculate_score(idea, industry),
        'market_size': estimate_market_size(industry),
        'competition': check_competition(idea),
        'trends': get_industry_trends(industry),
        'recommendations': generate_recommendations(idea),
        'risks': identify_risks(idea)
    }
    
    return analysis

def calculate_score(idea, industry):
    """Simple scoring algorithm"""
    score = 50  # Base score
    
    # Idea length factor
    if len(idea.split()) > 10:
        score += 10
    
    # Industry bonus
    hot_industries = ['AI', 'SaaS', 'Healthcare', 'Fintech']
    if industry in hot_industries:
        score += 15
    
    # Problem-solution check
    problem_keywords = ['solve', 'help', 'improve', 'reduce', 'automate']
    if any(keyword in idea.lower() for keyword in problem_keywords):
        score += 20
    
    return min(score, 100)

def estimate_market_size(industry):
    """Simple market size estimation"""
    sizes = {
        'Technology': 'Large',
        'Healthcare': 'Very Large',
        'Education': 'Large',
        'Finance': 'Large',
        'Retail': 'Very Large',
        'Other': 'Medium'
    }
    return sizes.get(industry, 'Medium')

def check_competition(idea):
    """Basic competition check"""
    keywords = idea.lower().split()
    if any(word in ['app', 'platform', 'software'] for word in keywords):
        return 'High'
    return 'Medium'

def get_industry_trends(industry):
    """Industry trends"""
    trends = {
        'Technology': 'AI integration, Remote work solutions',
        'Healthcare': 'Telemedicine, Health tech',
        'Education': 'EdTech, Online learning',
        'Finance': 'FinTech, Digital banking'
    }
    return trends.get(industry, 'Growing digital adoption')

def generate_recommendations(idea):
    """Generate recommendations"""
    recs = [
        "Validate with target customers",
        "Create MVP within 3 months",
        "Focus on one core feature first",
        "Research competitors thoroughly"
    ]
    return recs

def identify_risks(idea):
    """Identify potential risks"""
    risks = [
        "Market saturation",
        "High development costs",
        "User acquisition challenges"
    ]
    return risks