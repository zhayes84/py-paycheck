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

### Functions

- `overtime_rate(hourly_pay: float) -> float`: Calculates the hourly overtime pay rate.
- `was_overtime_accrued(num_hours_worked: float) -> bool`: Determines if overtime was accrued.
- `overtime_hours_accrued(num_hours_worked: float) -> float`: Calculates the number of hours accrued.
- `overtime_pay() -> float`: Calculates the overtime pay accrued.
- `tax_bracket(annual_income: float) -> int`: Determines the tax rate based on the employee's annual income.
- `tax_deduction(hourly_pay: float, num_hours_worked: float) -> float`: Calculates the amount of taxes to be deducted from gross pay.
- `take_home_pay(hourly_pay: float, num_hours_worked: float) -> float`: Calculates post-tax pay accrued.

## Example

```python
hourly_pay = 90
num_hours_worked = 41

take_home_pay = take_home_pay(hourly_pay, num_hours_worked)
print(f"Take Home Pay: ${take_home_pay}")
