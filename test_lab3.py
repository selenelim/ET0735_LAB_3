import pytest
from io import StringIO
from unittest.mock import patch

# Import functions from the script (assuming the script is named 'lab2.py')
from lab3 import get_user_input, calc_average, find_min_max


# Test for get_user_input function
@patch("builtins.input", return_value="5, 67, 32")
def test_get_user_input(mock_input):
    result = get_user_input()
    expected = [5.0, 67.0, 32.0]
    assert result == expected


# Test for calc_average function
def test_calc_average():
    data = [5.0, 67.0, 32.0]
    result = calc_average(data)
    expected = sum(data) / len(data)
    assert result == expected


# Test for find_min_max function
def test_find_min_max():
    data = [5.0, 67.0, 32.0]
    min_val, max_val = find_min_max(data)
    expected_min = min(data)
    expected_max = max(data)
    assert min_val == expected_min
    assert max_val == expected_max


# Optional: You can test the entire flow of the program as well.
# Here we will patch the input function to simulate user input and capture printed output.

@patch("builtins.input", return_value="5, 67, 32")
@patch("sys.stdout", new_callable=StringIO)
def test_main_program(mock_stdout, mock_input):
    from lab3 import main

    main()  # Call the main function
    output = mock_stdout.getvalue()

    # Check if specific output exists in the printed result
    assert "Average = " in output
    assert "Minimum is " in output
    assert "Maximum is " in output
    assert "*** End of program" in output
