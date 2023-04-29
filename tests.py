import pytest
from take_home_pay import (
    overtime_rate,
    was_overtime_accrued,
    overtime_hours_accrued,
    overtime_pay,
    tax_deduction,
    take_home_pay,
)


def test_overtime_rate():
    assert overtime_rate(90) == 135.0


def test_was_overtime_accrued():
    assert was_overtime_accrued(32) == False
    assert was_overtime_accrued(40) == False
    assert was_overtime_accrued(41) == True


def test_overtime_hours_accrued():
    assert overtime_hours_accrued(41) == 1
    assert overtime_hours_accrued(50) == 10


def test_overtime_pay():
    assert overtime_pay() == 135.0


def test_tax_deduction():
    assert tax_deduction(90, 32) == 1008.0
    assert tax_deduction(90, 41) == 1307.25


def test_take_home_pay():
    assert take_home_pay(90, 32) == 1872
    assert take_home_pay(90, 41) == 2427.75
