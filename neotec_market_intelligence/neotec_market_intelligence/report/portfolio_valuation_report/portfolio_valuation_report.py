def execute(filters=None):
    columns = [
        {"label": "Portfolio", "fieldname": "portfolio", "fieldtype": "Data", "width": 180},
        {"label": "Company", "fieldname": "company", "fieldtype": "Data", "width": 180},
        {"label": "Base Currency", "fieldname": "base_currency", "fieldtype": "Data", "width": 120},
        {"label": "Market Value", "fieldname": "market_value", "fieldtype": "Currency", "width": 140},
    ]
    data = []
    return columns, data
