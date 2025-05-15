import pytest
from employee_info import calculate_average_salary,get_employees_by_dept, get_employees_by_age_range

def test_calculate_average_salary():
    expected_result = 60166.67
    assert round(calculate_average_salary(), 2) == expected_result

def test_get_employees_by_dept():
    result = get_employees_by_dept("Engineering")
    expected_names = {"Chloe", "Mike"}

    actual_names = {emp["name"] for emp in result}
    
    assert actual_names == expected_names


def test_get_employees_by_age_range():
    # Test with a range that includes some employees
    result = get_employees_by_age_range(24, 36)
    expected_names = {"John", "Jane", "Mike", "Chloe"}
    result_names = {emp["name"] for emp in result}
    assert result_names == expected_names

    # Test with a range that includes only one employee
    result = get_employees_by_age_range(39, 41)
    expected_names = {"Peter"}
    result_names = {emp["name"] for emp in result}
    assert result_names == expected_names

