# take-home-pay

This project is a Python script that calculates the take-home pay for an employee given their hourly pay, number of hours worked, and tax rate. It also handles overtime pay calculations.

## Author
Zachary Hayes (c) 2023

## Functions

### overtime_rate

`overtime_rate(hourly_pay: float) -> float`

Calculates the hourly overtime pay rate.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **return (float)**: Returns the hourly overtime pay rate.

### was_overtime_accrued

`was_overtime_accrued(num_hours_worked: float) -> bool`

Determines if overtime was accrued.

- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return (bool)**: Boolean which is True if hours worked is greater than or equal to 41.

### overtime_hours_accrued

`overtime_hours_accrued(num_hours_worked: float) -> float`

Calculates the number of hours accrued.

- **num_hours_worked (float)**: Number of hours worked.
- **return (float)**: Number of hours worked subtracted by fourty.

### overtime_pay

`overtime_pay() -> float`

Calculates the overtime pay accrued.

- **return (float)**: Overtime pay rate multiplied by the number of overtime hours accrued.

### tax_deduction

`tax_deduction(hourly_pay: float, num_hours_worked: float)`

Calculates amount of taxes to be deducted from gross pay.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return**: Salary pay + overtime * tax_rate divided by 100.

### take_home_pay

`take_home_pay(hourly_pay: float, num_hours_worked: float) -> float`

Calculates post-tax pay accrued.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return (float)**: Income after deducting taxes.

## Example Usage

```python
hourly_pay = 90
num_hours_worked = 41
tax_rate = 35

print(take_home_pay(hourly_pay, num_hours_worked))
