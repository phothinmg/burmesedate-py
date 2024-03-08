#/* cSpell:disable */
import pytest
import burmesedate.burme as burme

class TestCheckYear:

    # Returns a dictionary with keys 'myt', 'tg1', 'fm', and 'werr' for valid input.
    def test_valid_input(self):
        # Initialize the year
        my_year = 1385

        # Invoke the `check_year` function
        result = burme.check_year(my_year)

        # Check if the result is a dictionary
        assert isinstance(result, dict)

        # Check if the result contains the expected keys
        assert "myt" in result
        assert "tg1" in result
        assert "fm" in result
        assert "werr" in result

    # Returns 'myt' as 0 for input year less than 638.
    def test_year_less_than_638(self):
        # Initialize the year
        my_year = 600

        # Invoke the `check_year` function
        result = burme.check_year(my_year)

        # Check if the value of 'myt' is 0
        assert result["myt"] == 0
