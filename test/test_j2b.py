#/* cSpell:disable */
import pytest

import burmesedate.burme as burme


class TestJulianToBurmese:

    # The function correctly converts a Julian Day Number to a Burmese date.
    def test_convert_julian_to_burmese(self):
        # Test with a Julian Day Number of 2459450.5
        result = burme.julian_to_burmese(2459450.5)
        assert result == {
            "myt": 0,
            "my": 1383,
            "mm": 5,
            "md": 17,
        }

        # Test with a Julian Day Number of 2459451.5
        result = burme.julian_to_burmese(2459451.5)
        assert result == {
            "myt": 0,
            "my": 1383,
            "mm": 5,
            "md": 18,
        }

    # The function correctly handles the minimum possible Julian Day Number.
    def test_handle_minimum_julian_day_number(self):
        # Test with the minimum possible Julian Day Number of -4713.5
        result = burme.julian_to_burmese(-4713.5)
        assert result == {
            "myt": 0,
            "my": -5363,
            "mm": 1,
            "md": 3,
        }
