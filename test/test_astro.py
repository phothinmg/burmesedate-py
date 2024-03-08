# /* cSpell:disable */
import pytest
import sys
import burmesedate.astro as astro

# check passed
class TestAstro:

    def test_sabbath_common_year(self):  # common year mty = 0
        # Arrange
        md = 14
        mm = 2
        myt = 0
        expected_result = 2  # eve

        # Act
        result = astro.calculate_sabbath(md, mm, myt)

        # Assert
        assert result == expected_result

    def test_sabbath_little_watat_year(self):  # little watat year mty = 1
        # Arrange
        md = 13
        mm = 2
        myt = 1
        expected_result = 0  # false

        # Act
        result = astro.calculate_sabbath(md, mm, myt)

        # Assert
        assert result == expected_result

    def test_sabbath_big_watat_year(self):  # big watat year mty = 1
        # Arrange
        md = 23
        mm = 2
        myt = 2
        expected_result = 1  # sabbath

        # Act
        result = astro.calculate_sabbath(md, mm, myt)

        # Assert
        assert result == expected_result

    def test_yatyaza(self):
        # Arrange
        mm = 11
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_yatyaza(mm, wd)

        # Assert
        assert result == expected_result

    def test_pyathada(self):
        # Arrange
        mm = 8
        wd = 3
        expected_result = 1

        # Act
        result = astro.calculate_pyathada(mm, wd)

        # Assert
        assert result == expected_result

    def test_nagahle(self):
        # Arrange
        mm = 7
        expected_result = 2

        # Act
        result = astro.calculate_nagahle(mm)

        # Assert
        assert result == expected_result

    def test_mahabote(self):
        # Arrange
        mm = 8
        wd = 3
        expected_result = 5

        # Act
        result = astro.calculate_mahabote(mm, wd)

        # Assert
        assert result == expected_result

    def test_nakhat(self):
        # Arrange
        my = 1385
        expected_result = 2

        # Act
        result = astro.calculate_nakhat(my)

        # Assert
        assert result == expected_result

    def test_thamanyo(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_thamanyo(mm, wd)

        # Assert
        assert result == expected_result

    def test_amyeittasote(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_amyeittasote(mm, wd)

        # Assert
        assert result == expected_result

    def test_warameittugyi(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_warameittugyi(mm, wd)

        # Assert
        assert result == expected_result

    def test_warameittunge(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_warameittunge(mm, wd)

        # Assert
        assert result == expected_result

    def test_yatpote(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_yatpote(mm, wd)

        # Assert
        assert result == expected_result

    def test_thamaphyu(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_thamaphyu(mm, wd)

        # Assert
        assert result == expected_result

    def test_nagapor(self):
        # Arrange
        mm = 7
        wd = 2
        expected_result = 0

        # Act
        result = astro.calculate_nagapor(mm, wd)

        # Assert
        assert result == expected_result

    def test_yatyotema(self):
        # Arrange
        mm = 7
        md = 18
        expected_result = 0

        # Act
        result = astro.calculate_yatyotema(mm, md)

        # Assert
        assert result == expected_result

    def test_mahayatkyan(self):
        # Arrange
        mm = 7
        md = 18
        expected_result = 0

        # Act
        result = astro.calculate_mahayatkyan(mm, md)

        # Assert
        assert result == expected_result

    def test_shanyat(self):
        # Arrange
        mm = 7
        md = 18
        expected_result = 1

        # Act
        result = astro.calculate_shanyat(mm, md)

        # Assert
        assert result == expected_result

    def test_cal_astro_days(self):
        # Arrange
        jd = 2361222
        expected_result = ['Thamanyo']

        # Act
        result = astro.calculate_astro_days(jd)

        # Assert
        assert result == expected_result
