daily_rate = 100

month_days = {
    "jan": 31, "feb": 28, "mar": 31,
    "apr": 30, "may": 31, "jun": 30,
    "jul": 31, "aug": 31, "sep": 30,
    "oct": 31, "nov": 30, "dec": 31
}

all_months_in_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                       'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def get_quarter_payment(start_month):
    start_month = start_month.strip().lower()[:3]
    if start_month not in month_days:
        return f"❌ Invalid month: {start_month}"

    idx = all_months_in_order.index(start_month)
    quarter_months = [all_months_in_order[(idx + i) % 12] for i in range(3)]

    total_payment = sum(month_days[m] * daily_rate for m in quarter_months)
    months_str = ", ".join(m.capitalize() for m in quarter_months)

    return f"💰🐱‍👓🚎 Payment for quarter starting in {start_month.capitalize()} ({months_str}): ₹{total_payment}"

# Example usage:
user_input = input("Enter quarter start month (e.g., jan, apr, jul, oct): ")
result = get_quarter_payment(user_input)
print(result)
