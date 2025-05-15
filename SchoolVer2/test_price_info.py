import pytest
from price_info import total_cost_shopping, cost_of_fruits


def test_cost_of_fruits():
    assert cost_of_fruits('apple',10)== 12
    assert cost_of_fruits('orange',4)== 5.6


def test_total_cost_shopping():
    expected_total = (1.2*5) + (1.4*5) + (6.5*1) + (2.7*2) + (0.9*10) + (2.95*1) + (4.95*2)

    assert total_cost_shopping()== expected_total

