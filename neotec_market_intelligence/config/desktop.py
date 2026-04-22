from frappe import _

def get_data():
    return [
        {
            "module_name": "Neotec Market Intelligence",
            "category": "Modules",
            "label": _("Neotec Market Intelligence"),
            "color": "grey",
            "icon": "octicon octicon-graph",
            "type": "module",
            "description": _("Treasury, portfolio, and market intelligence workspace")
        }
    ]
