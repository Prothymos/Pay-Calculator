def pay(hours, pay_rate):
    gross_pay = 0
    if time <= 40:
        gross_pay = hours * pay_rate
    elif time > 40:
        normal_pay = 40 * pay_rate
        overtime_pay = (hours - 40) * (pay_rate * 1.5)
        gross_pay = normal_pay + overtime_pay
    return gross_pay
