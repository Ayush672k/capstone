def check_domain_availability(names):
    """Mock domain checker: marks .com available for even-indexed names."""
    out = {}
    for i, name in enumerate(names):
        n = name.lower().replace(' ', '')
        out[name] = {
            '.com': {'domain': f'{n}.com', 'available': (i % 2 == 0)},
            '.ai': {'domain': f'{n}.ai', 'available': True}
        }
    return out
