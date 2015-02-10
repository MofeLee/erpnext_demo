app_name = "erpnext_demo"
app_title = "ERPNext Demo"
app_publisher = "Web Notes Technlogies"
app_description = "Demo Builder"
app_icon = "icon-coffee"
app_color = "#d6cec3"
app_email = "info@erpnext.com"
app_url = "http://erpnext.org"
app_version = "0.0.1"
hide_in_installer = True

before_install = "erpnext_demo.utils.check_if_not_setup"
after_install = "erpnext_demo.utils.make_demo"

on_session_creation = "erpnext_demo.utils.on_login"

app_include_js = "assets/erpnext_demo/js/desktop.js"

doc_events = {
	"User": {
		"validate_reset_password": "erpnext_demo.utils.validate_reset_password"
	}
}

# fixture = "Account"
# fixture = "Address"
# fixture = "BOM"
# fixture = "Contact"
# fixture = "Customer"
# fixture = "Employee"
# fixture = "Fiscal Year"
# fixture = "Item"
# fixture = "Item Price"
# fixture = "Lead"
# fixture = "Salary Structure"
# fixture = "Sales Taxes and Charges Master"
# fixture = "Shipping Rule"
# fixture = "Shopping Cart Settings"
# fixture = "Supplier"
# fixture = "User"
