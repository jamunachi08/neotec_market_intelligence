# Neotec Market Intelligence v2

ERPNext-native treasury, portfolio, and market intelligence app.

## v2 highlights
- Correct Frappe module layout for installation compatibility
- Treasury and FX exposure doctypes
- Alert events and proposal workflows scaffolding
- Scenario and AI insight doctypes
- Starter workspace/workflow fixtures
- Scheduler-safe services and provider abstraction

## Installation notes
This app expects ERPNext v15 / Frappe v15.

If installing from a local path:
```bash
bench get-app file:///path/to/neotec_market_intelligence
bench --site yoursite install-app neotec_market_intelligence
```

## Important packaging fix
The app now includes the required inner module package:
`neotec_market_intelligence/neotec_market_intelligence/`
so Frappe can import `neotec_market_intelligence.neotec_market_intelligence` during sync.
