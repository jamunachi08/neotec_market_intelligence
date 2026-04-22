frappe.pages['research-workbench'].on_page_load = function(wrapper) {
    frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Research Workbench',
        single_column: true,
    });
    $(wrapper).find('.layout-main-section').html(
        '<div class="nmi-card" style="padding: 20px; border: 1px solid var(--border-color);">' +
        '<h4>Research Workbench</h4>' +
        '<p>Starter page placeholder. Replace this with dashboard widgets, charts, tables, and filters.</p>' +
        '</div>'
    );
};
