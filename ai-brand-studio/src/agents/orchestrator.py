from src.agents.name_generator import generate_names
from src.tools.domain_checker import check_domain_availability
from src.tools.trademark_checker import search_trademarks_mock
from src.tools.seo import analyze_seo

def run_pipeline(brief):
    names = generate_names(brief, n=20)
    domains = check_domain_availability(names)
    validation = []
    for nm in names:
        tm = search_trademarks_mock(nm)
        seo = analyze_seo(nm, ' '.join(brief.split()[:6]))
        validation.append({
            'name': nm,
            'domain': domains.get(nm, {}),
            'trademark': tm,
            'seo': seo
        })
    final = [v for v in validation if v['trademark']['risk_level']=='low' and any(ext['available'] for ext in v['domain'].values())]
    return {'brief': brief, 'candidates': final[:10], 'all': validation}
