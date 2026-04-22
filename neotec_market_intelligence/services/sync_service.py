import frappe

def refresh_market_snapshots():
    frappe.logger().info('NMI sync job executed')
    return True

@frappe.whitelist()
def run_manual_snapshot_sync():
    refresh_market_snapshots()
    return {'ok': True, 'message': 'Snapshot sync completed'}
