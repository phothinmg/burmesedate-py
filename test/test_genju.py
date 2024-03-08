#/* cSpell:disable */
import datetime
import pytest
import burmesedate.genju as genju

class TestGregorianToJulian:

    # The function returns the correct Julian date for a valid Gregorian date.
    def test_valid_gregorian_date(self):
        # Arrange
        year = 2022
        month = 12
        day = 31

        # Act
        result = genju.gregorian_to_julian(year, month, day)

        # Assert
        assert result == 2459945.5

    # The function raises a ValueError if the month is less than 1.
    def test_invalid_month(self):
        # Arrange
        year = 2022
        month = -1
        day = 31

        # Act & Assert
        with pytest.raises(ValueError):
            genju.gregorian_to_julian(year, month, day)

    # The function correctly converts a Julian date to a Gregorian date.

    def test_convert_julian_to_gregorian(self):
        # Arrange
        julian_date = 2459450.5
        expected_date = datetime.date(2021, 8, 23)

        # Act
        result = genju.julian_to_gregorian(julian_date)

        # Assert
        assert result == expected_date

    # # The function correctly handles input that is not a float.
    # def test_handle_non_float_input(self):
    #     # Arrange
    #     julian_date = "2459450.5"

    #     # Act and Assert
    #     with pytest.raises(TypeError):
    #         julian_to_gregorian(julian_date)
