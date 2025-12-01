import json
from src.agents.orchestrator import run_pipeline
TESTS = [
    ('healthcare mental wellness app for gen z', 15),
    ('fintech expense tracker for freelancers', 15),
    ('enterprise inventory management for retailers', 15),
]
def run_all():
    reports = {}
    for brief, min_names in TESTS:
        res = run_pipeline(brief)
        reports[brief] = {'candidates_count': len(res['all']), 'meets_min': len(res['all'])>=min_names}
    with open('results/sample_eval_report.json','w') as f:
        json.dump(reports,f,indent=2)
    print('Wrote results/sample_eval_report.json')
if __name__ == '__main__':
    run_all()
