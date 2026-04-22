# Developer Guide

## Mandatory Frappe packaging rule
Because the module in `modules.txt` is `Neotec Market Intelligence`, Frappe scrubs it to
`neotec_market_intelligence` and imports:

`neotec_market_intelligence.neotec_market_intelligence`

That means the repository must include the nested package:

- neotec_market_intelligence/
  - __init__.py
  - neotec_market_intelligence/
    - __init__.py
    - doctype/
    - page/
    - report/

## v2 scope
- Market data foundation
- Treasury book and FX exposure
- Investment and rebalance proposals
- Alert events
- Scenario models
- AI insight records

## Next implementation targets
1. Add child tables for watchlists, portfolio lines, hedge mappings, and allocation targets.
2. Export real workflows from a dev site instead of placeholder fixture JSON.
3. Add Workspace JSON export from a live site.
4. Add dashboard charts and number cards.
5. Add real provider adapters and secure credential storage.
6. Add Arabic translations and role-specific workspaces.
