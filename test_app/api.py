import frappe

@frappe.whitelist()
def execute_function(*args,**kwargs):
    """
    This fonction will be executed when the Execute Action Button will be clicked
    """
    print('Hello World')
    # The data is transmitted via keyword argument
    print(kwargs)


@frappe.whitelist()
def execute_buy_function(*args,**kwargs):
    """
    This fonction will be executed when the Execute Action Button will be clicked
    """
    print('Hello World')
    # The data is transmitted via keyword argument
    print(kwargs)