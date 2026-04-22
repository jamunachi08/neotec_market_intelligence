import frappe

def evaluate_alert_rules():
    frappe.logger().info('NMI alert evaluation executed')
    return True

@frappe.whitelist()
def generate_test_alert(message='Test alert from NMI'):
    doc = frappe.get_doc({
        'doctype': 'NMI Alert Event',
        'alert_rule': None,
        'message': message,
        'status': 'Open',
        'severity': 'Medium'
    })
    return {'ok': True, 'message': 'Test alert prepared', 'doc': doc.as_dict()}
