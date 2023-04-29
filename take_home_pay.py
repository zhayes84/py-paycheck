# take-home-pay by Zachary Hayes (c) 2023
hourly_pay: float = 90  # value can sometimes be float
num_hours_worked: float = 41
tax_rate: int = 35


def overtime_rate(hourly_pay: float) -> float:
    """Calculates the hourly overtime pay rate.

    Multiplies the the hourly pay by 1.5 to determine
    the hourly overtime pay rate.

    :param hourly_pay: The hourly pay rate for a given employee.
    :type hourly_pay: float
    :return: Returns the hourly overtime pay rate.
    :rtype: float
    """
    return hourly_pay * 1.5


def was_overtime_accrued(num_hours_worked: float) -> bool:
    """Determines if overtime was accrued.

    Subtracts the number of hours worked by 40. If there is a
    remainder of hours, this means overtime pay was accrued.
    This function is used by take_home_pay().

    :param num_hours_worked: The number of hours worked by an employee.
    :type num_hours_worked: float
    :return: Boolean which is True if hours worked is greater than or
        equal to 41.
    :rtype: bool
    """
    if num_hours_worked >= 41:
        return True
    else:
        return False


def overtime_hours_accrued(num_hours_worked: float) -> float:
    """Calculates the number of hours accrued.

    Subtracts the number of hours worked by 40 to isolate the
    number of overtime hours worked. This function is only
    called if was_overtime_accrued() returns True.

    :param num_hours_worked: Number of hours worked.
    :type num_hours_worked: float
    :return: Number of hours worked subtracted by fourty.
    :rtype: float
    """
    return num_hours_worked - 40


def overtime_pay() -> float:
    """Calculates the overtime pay accrued.

    Calls overtime_rate() to determine the hourly pay rate
    and calls overtime_hours_accrued() to to determine what
    number to multiply to the hourly pay rate. The product
    of the two is the gross overtime pay.

    :return: Overtime pay rate multiplied by the number of overtime hours accrued.
    :rtype: float
    """
    return overtime_rate(hourly_pay) * overtime_hours_accrued(num_hours_worked)


def tax_deduction(hourly_pay: float, num_hours_worked: float):
    """Calculates amount of taxes to be deducted from gross pay.

    Multiplies hourly_pay by fourty to determine gross pre-overtime
    pay, adds gross pre-overtime pay to overtime pay accrued,
    multiplied by tax_rate, and divided by 100 to calculate the
    amount of taxes to be deducted from gross pay.

    :param hourly_pay: The hourly pay rate for a given employee.
    :type hourly_pay: float
    :return: Salary pay + overtime * tax_rate divided by 100.
    :rtype: _type_
    """

    if was_overtime_accrued(num_hours_worked):  # if True
        salary_pay: float = hourly_pay * 40
        ot: float = overtime_pay()
        return ((salary_pay + ot) * tax_rate) / 100
    else:
        return ((num_hours_worked * hourly_pay) * tax_rate) / 100


def take_home_pay(hourly_pay: float, num_hours_worked: float) -> float:
    """Calculates post-tax pay accrued.

    If overtime was accrued, take_home_pay() adds pre-overtime income
    to post-overtime income, subtracted by the tax_deduction(). If no
    overtime was accrued, take_home_pay() subtracts the tax_deduction
    from pre-overtime income.

    :param hourly_pay: The hourly pay rate for a given employee.
    :type hourly_pay: float
    :return: Income after deducting taxes.
    :rtype: float
    """

    if was_overtime_accrued(num_hours_worked):  # if True = overtime earned
        salary_pay: float = hourly_pay * 40
        return salary_pay + overtime_pay() - tax_deduction(hourly_pay, num_hours_worked)
    else:  # no overtime earned
        salary_pay = hourly_pay * num_hours_worked
        return salary_pay - tax_deduction(hourly_pay, num_hours_worked)


if __name__ == "__main__":
    take_home_pay(hourly_pay, num_hours_worked)


# print(
#     f"Hourly Pay: ${hourly_pay}\n"
#     f"Number of Hours Worked: {num_hours_worked}\n"
#     f"Tax Rate: {tax_rate}%\n\n"
#     f"Overtime Pay Rate: ${overtime_rate(hourly_pay)}\n"
#     f"Overtime Accrued? {was_overtime_accrued(num_hours_worked)}\n"
#     f"Take Home Pay: ${take_home_pay(hourly_pay, num_hours_worked)}"
# )
