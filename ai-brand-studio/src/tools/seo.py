def analyze_seo(name, context):
    # Simple heuristic scoring (mock)
    score = 50
    if len(name) <= 10:
        score += 20
    if any(k in name.lower() for k in ['app','ai','tech','hub']):
        score += 10
    if any(w.lower() in name.lower() for w in context.split()):
        score += 5
    return {'seo_score': min(100, score)}
