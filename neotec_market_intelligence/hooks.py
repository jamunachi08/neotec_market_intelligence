app_name = "neotec_market_intelligence"
app_title = "Neotec Market Intelligence"
app_publisher = "OpenAI"
app_description = "ERPNext-native treasury, portfolio, and market intelligence app"
app_email = "support@example.com"
app_license = "MIT"

required_apps = ["frappe", "erpnext"]

app_include_css = [
    "/assets/neotec_market_intelligence/css/nmi.css",
]

app_include_js = [
    "/assets/neotec_market_intelligence/js/nmi.js",
]

fixtures = [
    {"dt": "Workspace", "filters": [["module", "=", "Neotec Market Intelligence"]]},
    {"dt": "Workflow", "filters": [["document_type", "in", ["NMI Investment Proposal", "NMI Rebalance Proposal", "NMI Alert Event"]]]},
    {"dt": "Custom Field", "filters": [["module", "=", "Neotec Market Intelligence"]]},
]

scheduler_events = {
    "cron": {
        "*/15 * * * *": [
            "neotec_market_intelligence.services.sync_service.refresh_market_snapshots"
        ],
        "0 * * * *": [
            "neotec_market_intelligence.services.alert_service.evaluate_alert_rules"
        ],
        "15 1 * * *": [
            "neotec_market_intelligence.services.valuation_service.refresh_daily_valuation_cache"
        ]
    }
}
