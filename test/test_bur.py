#/* cSpell:disable */

import pytest
import burmesedate.burme as burme


class TestCalculateMonthLength:

    # Returns 30 for even months (Tagu, Nayon, Wagaung, Tazaungmon, Pyatho)
    # [Tagu=1, Kason=2, Nayon=3,1st Waso=0, (2nd) Waso=4, Wagaung=5, Tawthalin=6,Thadingyut=7, Tazaungmon=8, Nadaw=9, Pyatho=10, Tabodwe=11,Tabaung=12, Late Tagu=13, Late Kason=14]
    def test_odd_months_common_year(self):
        assert burme.calculate_month_length(1, 0) == 29
        assert burme.calculate_month_length(3, 0) == 29
        assert burme.calculate_month_length(5, 0) == 29
        assert burme.calculate_month_length(7, 0) == 29
        assert burme.calculate_month_length(9, 0) == 29
        assert burme.calculate_month_length(11, 0) == 29
        assert burme.calculate_month_length(13, 0) == 29

    def test_even_months_common_year(self):
        assert burme.calculate_month_length(0, 0) == 30
        assert burme.calculate_month_length(2, 0) == 30
        assert burme.calculate_month_length(4, 0) == 30
        assert burme.calculate_month_length(6, 0) == 30
        assert burme.calculate_month_length(8, 0) == 30
        assert burme.calculate_month_length(10, 0) == 30
        assert burme.calculate_month_length(14, 0) == 30

    # Returns 29 for Tagu month and little watat year type.
    def test_tagu_month_little_watat_year(self):
        assert burme.calculate_month_length(1, 1) == 29


class TestCalculateMoonPhase:

    # Should return 0 when given md=15, mm=1, myt=0
    def test_return_0_when_given_md_15_mm_1_myt_0(self):
        assert burme.calculate_moon_phase(15, 1, 0) == 1

    # Should return 3 when given md=30, mm=12, myt=0
    def test_return_3_when_given_md_30_mm_12_myt_0(self):
        assert burme.calculate_moon_phase(30, 12, 0) == 3


class TestCalculateFortnightDay:

    def test_returns_1_when_given_1_as_input(self):
        assert burme.calculate_fortnight_day(1) == 1

    def test_returns_1_when_given_20_as_input(self):
        assert burme.calculate_fortnight_day(20) == 5

    def test_returns_1_when_given_15_as_input(self):
        assert burme.calculate_fortnight_day(15) == 15

    def test_returns_1_when_given_14_as_input(self):
        assert burme.calculate_fortnight_day(14) == 14

    def test_returns_1_when_given_14_as_input(self):
        assert burme.calculate_fortnight_day(30) == 15

    def test_returns_error_when_given_0_as_input(self):
        assert burme.calculate_fortnight_day(0) == 0


class TestCalculateYearLength:
    # types of Burmese year [0=common, 1=little watat, 2=big watat]
    def test_for_common_year_myt0(self):
        assert burme.calculate_year_length(0) == 354

    def test_for_little_watat_year_myt1(self):
        assert burme.calculate_year_length(1) == 384

    def test_for_big_watat_year_myt2(self):
        assert burme.calculate_year_length(2) == 385


class TestCalculateDayInMonth:
    # Moon phase [0=waxing, 1=full moon, 2=waning, 3=new moon]
    # types of Burmese year [0=common, 1=little watat, 2=big watat]
    # mp 0 mf 1 to 14
    def test_mp0_waxing(self):
        assert burme.calculate_day_in_month(1, 0, 2, 0) == 1  # common year
        assert  burme.calculate_day_in_month(10, 0, 5, 1) == 10  # little watat year
        assert  burme.calculate_day_in_month(14, 0, 11, 2) == 14  # big watat year

    # Test for MP = 1 full moon for all year types and different day and month
    # mf 1 to 14 only
    def test_mp1_full_moon(self):
        assert  burme.calculate_day_in_month(1, 1, 2, 0) == 15  # common year
        assert  burme.calculate_day_in_month(10, 1, 5, 1) == 15  # little watat year
        assert  burme.calculate_day_in_month(14, 1, 11, 2) == 15  # big watat year
    # mp 2 mf 1 to 14

    def test_mp2_waning(self):
        assert  burme.calculate_day_in_month(1, 2, 2, 0) == 16  # common year
        assert  burme.calculate_day_in_month(10, 2, 5, 1) == 25  # little watat year
        assert  burme.calculate_day_in_month(14, 2, 11, 2) == 29  # big watat year
    # mp 3 mf 1 to 14

    def test_mp3_new_moon(self):
        assert  burme.calculate_day_in_month(1, 3, 2, 0) == 30  # common year
        assert  burme.calculate_day_in_month(10, 3, 5, 1) == 29  # little watat year
        assert  burme.calculate_day_in_month(14, 3, 11, 2) == 29  # big watat year
    # mf 15 , myt 0

    def test_mf15_myt0(self):
        assert  burme.calculate_day_in_month(15, 0, 2, 0) == 15  # waxing
        assert  burme.calculate_day_in_month(15, 1, 5, 0) == 15  # full moon
        assert  burme.calculate_day_in_month(15, 2, 11, 0) == 30  # waning
        assert burme.calculate_day_in_month(15, 3, 11, 0) == 29  # new moon

    # mf 15 , myt 1
    def test_mf15_myt1(self):
        assert  burme.calculate_day_in_month(15, 0, 2, 1) == 15  # waxing
        assert  burme.calculate_day_in_month(15, 1, 5, 1) == 15  # full moon
        assert  burme.calculate_day_in_month(15, 2, 11, 1) == 30  # waning
        assert  burme.calculate_day_in_month(15, 3, 11, 1) == 29  # new moon
    # mf 15 , myt 2

    def test_mf15_myt2(self):
        assert  burme.calculate_day_in_month(15, 0, 2, 2) == 15  # waxing
        assert  burme.calculate_day_in_month(15, 1, 5, 2) == 15  # full moon
        assert burme.calculate_day_in_month(15, 2, 11, 2) == 30  # waning
        assert  burme.calculate_day_in_month(15, 3, 11, 2) == 29  # new moon


class TestBurmeseToJulian:

    # Converts a valid Burmese date to a Julian Day Number.
    def test_valid_burmese_date_to_julian(self):
        # Arrange
        my = 1385
        mm = 7
        md = 15
        expected_jdn = 2460247

        # Act
        result = burme.burmese_to_julian(my, mm, md)

        # Assert
        assert result == expected_jdn

    # Handles the earliest possible Burmese date correctly (year 0).
    def test_earliest_burmese_date_to_julian(self):
        # Arrange
        my = 0
        mm = 1
        md = 1
        expected_jdn = 1954167

        # Act
        result = burme.burmese_to_julian(my, mm, md)

        # Assert
        assert result == expected_jdn
