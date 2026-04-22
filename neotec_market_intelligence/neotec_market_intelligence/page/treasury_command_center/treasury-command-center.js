frappe.pages['treasury-command-center'].on_page_load = function(wrapper) {
    frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Treasury Command Center',
        single_column: true,
    });
    $(wrapper).find('.layout-main-section').html(
        '<div class="nmi-card" style="padding: 20px; border: 1px solid var(--border-color);">' +
        '<h4>Treasury Command Center</h4>' +
        '<p>Starter page placeholder. Replace this with dashboard widgets, charts, tables, and filters.</p>' +
        '</div>'
    );
};
