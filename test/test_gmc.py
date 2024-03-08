#/* cSpell:disable */
import pytest
import burmesedate.burme as burme


class TestGetMyConst:

    # Returns a dictionary with the calculated constants for a given Burmese year.
    def test_returns_dictionary_with_calculated_constants(self):
        # Arrange
        my = 1385

        # Act
        result = burme.get_my_const(my)

        # Assert
        assert isinstance(result, dict)
        assert "ei" in result
        assert "wo" in result
        assert "nm" in result
        assert "ew" in result

    # Returns correct constants for the earliest possible Burmese year (ME 0).
    def test_returns_correct_constants_for_earliest_year(self):
        # Arrange
        my = 0

        # Act
        result = burme.get_my_const(my)

        # Assert
        assert result["ei"] == 1.1
        assert result["wo"] == -1.1
        assert result["nm"] == -1
        assert result["ew"] == 0
