import frappe
from frappe import _
from frappe.utils.data import date_diff, today


def successful_login(login_manager):
    """
    on_login verify if details in employee are filled and also Direct Deposit Authorization is filled
    """
    if frappe.db.exists("Employee", {"user_id":frappe.session.user}):
        employee = frappe.get_doc('Employee', {'user_id': frappe.session.user})
        
        if employee:
            if not employee.person_to_be_contacted or not employee.emergency_phone_number \
                    or not employee.relation:
                frappe.cache().hset("redirect_after_login", login_manager.user, f"app/employee/{employee.name}")
                frappe.msgprint("Welcome to Frappe ERPNext! Please fill in your emergency contact details.")

            # if not employee.passport_number:
            #     frappe.local.response['type'] = 'redirect'
            #     frappe.local.response['location'] = f'/desk#Form/Employee/{employee.name}'
            #     frappe.msgprint("Welcome to Frappe ERPNext! Please fill in your emergency contact details.")
