type = "Quaterly wise"
transfer_type = "(Quaterly wise) jan , april , jul , oct "
daily_rate = 100 

month_days = {
    "jan": 31, "january": 31,
    "feb": 28, "february": 28,
    "mar": 31, "march": 31,
    "apr": 30, "april": 30,
    "may": 31,
    "jun": 30, "june": 30,
    "jul": 31, "july": 31,
    "aug": 31, "august": 31,
    "sep": 30, "september": 30,
    "oct": 31, "october": 31,
    "nov": 30, "november": 30,
    "dec": 31, "december": 31,
}

if type.lower() in transfer_type.lower():

    month_part = transfer_type.split(')')[-1]
    quarter_months = [m.strip().lower()[:3] for m in month_part.split(',') if m.strip().lower()[:3] in month_days]

    print("Quarterly start months:", quarter_months)

    all_months_in_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                           'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    total_quarter_payments = {}

    for q in quarter_months:
        try:
            idx = all_months_in_order.index(q)
            next_three = [all_months_in_order[(idx + i) % 12] for i in range(3)]
            total_payment = sum(month_days[m] * daily_rate for m in next_three)
            total_quarter_payments[q] = {
                "months": next_three,
                "amount": total_payment
            }
        except ValueError:
            print(f"❌ Invalid month: {q}")

    for start_month, data in total_quarter_payments.items():
        months_str = ", ".join(m.capitalize() for m in data["months"])
        print(f"💰😎 Payment for quarter starting in {start_month.capitalize()} ({months_str}): ₹{data['amount']}")