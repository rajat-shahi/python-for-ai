def calculate_total(quantity, price):
    """calculate total for a single item"""
    return quantity*price

def format_currency(amount):
    """format number as currency"""
    return f"${amount:,.2f}"