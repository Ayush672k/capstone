def search_trademarks_mock(brand_name):
    """Very small mock: flags names containing 'corp' or 'inc' as high risk."""
    lower = brand_name.lower()
    if 'corp' in lower or 'inc' in lower:
        return {'brand_name': brand_name, 'risk_level': 'high', 'conflicts': ['FakeCorp']}
    return {'brand_name': brand_name, 'risk_level': 'low', 'conflicts': []}
