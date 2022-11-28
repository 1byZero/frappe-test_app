import frappe
from frappe.utils import now

@frappe.whitelist()
def execute_function(*args,**kwargs):
    """
    This function will be executed when the Execute Action Button will be clicked
    """
    whois = now()
    
    frappe.msgprint(

         msg= whois,
         title='Succesful Message',
       
    ) 

@frappe.whitelist()
def execute_buy_function(*args,**kwargs):
    
    frappe.msgprint(
         msg='Feature Coming Soon',
         title='Domain Buy Coming Soon', 
    )