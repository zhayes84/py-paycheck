# Take-Home-Pay Calculator by Zachary Hayes (c) 2023

This program calculates an employee's take-home pay based on their hourly pay, the number of hours worked, and the applicable tax rate determined by their annual income.

## Features

- Calculates hourly overtime pay rate
- Determines if overtime was accrued
- Calculates overtime hours accrued
- Calculates overtime pay
- Determines tax bracket based on annual income
- Calculates tax deductions
- Calculates take-home pay

## Usage

1. Set the `hourly_pay` and `num_hours_worked` variables.
2. The program will calculate the take-home pay for the given employee, considering their hourly pay, hours worked, and tax bracket.

### Variables

- `hourly_pay`: (float) The hourly pay rate for a given employee.
- `num_hours_worked`: (float) The number of hours worked by an employee.
- `TAX_BRACKETS`: (List[Tuple[float, float]]) A list of tuples representing the tax brackets and their corresponding tax rates.

## Functions

### overtime_rate
`overtime_rate(hourly_pay: float) -> float`

Calculates the hourly overtime pay rate.

Multiplies the the hourly pay by 1.5 to determine the hourly overtime pay rate.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **return (float)**: Returns the hourly overtime pay rate.

### was_overtime_accrued

`was_overtime_accrued(num_hours_worked: float) -> bool`

Determines if overtime was accrued.

Subtracts the number of hours worked by 40. If there is a remainder of hours, this means overtime pay was accrued. This function is used by take_home_pay().

- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return (bool)**: Boolean which is True if hours worked is greater than or equal to 41.

### overtime_hours_accrued

`overtime_hours_accrued(num_hours_worked: float) -> float`

Calculates the number of hours accrued.

Subtracts the number of hours worked by 40 to isolate the number of overtime hours worked. This function is only called if was_overtime_accrued() returns True.

- **num_hours_worked (float)**: Number of hours worked.
- **return (float)**: Number of hours worked subtracted by fourty.

### overtime_pay

`overtime_pay() -> float`

Calculates the overtime pay accrued.

Calls overtime_rate() to determine the hourly pay rate and calls overtime_hours_accrued() to to determine what number to multiply to the hourly pay rate. The product of the two is the gross overtime pay.

- **return (float)**: Overtime pay rate multiplied by the number of overtime hours accrued.

### tax_bracket

`tax_bracket(annual_income: float) -> int:`

Determines the tax rate based on the employee's annual income.

- **annual_income (float)**: The employee's annual income.
- **return**: The tax rate for the given income.

### tax_deduction

`tax_deduction(hourly_pay: float, num_hours_worked: float)`

Calculates amount of taxes to be deducted from gross pay.

Multiplies hourly_pay by fourty to determine gross pre-overtime pay, adds gross pre-overtime pay to overtime pay accrued, multiplied by tax_rate, and divided by 100 to calculate the amount of taxes to be deducted from gross pay.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return**: Salary pay + overtime * tax_rate divided by 100.

### take_home_pay

`take_home_pay(hourly_pay: float, num_hours_worked: float) -> float`

Calculates post-tax pay accrued.

If overtime was accrued, take_home_pay() adds pre-overtime income to post-overtime income, subtracted by the tax_deduction(). If no overtime was accrued, take_home_pay() subtracts the tax_deduction from pre-overtime income.

- **hourly_pay (float)**: The hourly pay rate for a given employee.
- **num_hours_worked (float)**: The number of hours worked by an employee.
- **return (float)**: Income after deducting taxes.

## Example

```python
hourly_pay = 90
num_hours_worked = 41

take_home_pay = take_home_pay(hourly_pay, num_hours_worked)
print(f"Take Home Pay: ${take_home_pay}")
