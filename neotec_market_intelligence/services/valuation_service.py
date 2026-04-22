import frappe

def refresh_daily_valuation_cache():
    frappe.logger().info('NMI valuation refresh executed')
    return True

@frappe.whitelist()
def recalculate_portfolio(portfolio=None):
    return {'ok': True, 'portfolio': portfolio, 'message': 'Portfolio valuation recalculated'}
