from frappe.model.document import Document

class NmiAlertEvent(Document):
    def validate(self):
        if hasattr(self, 'exposure_amount') and hasattr(self, 'hedged_amount'):
            self.net_open_exposure = (self.exposure_amount or 0) - (self.hedged_amount or 0)
