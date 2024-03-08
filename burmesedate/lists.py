# /* cSpell:disable */

"""
Lists
"""


def set_weekdays():
    """
    List of weekdays.
    0 to 6

    Returns:
        list: A list of strings representing the weekdays.
    """
    return [

        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",

    ]


def set_months():
    """
    List of months.

    Returns:
        list: A list of strings representing the months.
    """
    return [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]


def set_burmese_months():
    """
    List of Burmese months.
    0 to 14

    Returns:
        list: A list of strings representing the Burmese months.
    """
    return [
        "1st_Waso",
        "Tagu",
        "Kason",
        "Nayon",
        "2nd_Waso",
        "Wagaung",
        "Tawthalin",
        "Thadingyut",
        "Tazaungmon",
        "Nadaw",
        "Pyatho",
        "Tabodwe",
        "Tabaung",
        "Late_Tagu",
        "Late_Kason"
    ]


def set_year_types():
    """
    List of year types.
    0 to 2

    Returns:
        list: A list of strings representing the year types.
    """
    return [
        "Common Year",
        "Little Watat Year",
        "Big Watat Year"
    ]


def set_sabbath():
    """
    List for Sabbath Calculation 
    0 to 2

    Returns:
        list: A list of strings representing the sabbath.
    """
    return [
        "false",
        "Sabbath",
        "Sabbath Eve"
    ]


def set_yatyaza():
    """ 
    List for Yatyaza Calculation

    Return:
        list: A list of strings representing the Yatyaza
    """
    return [
        "false",
        "Yatyaza"
    ]


def set_pyathada():
    """ 
    List for Pyathada Calculation
    0 to 2

    Return:
        list: A list of strings representing the Pyathada
    """
    return [
        "false",
        "Pyathada",
        "Afternoon Pyathada"
    ]


def set_nagahle():
    """ 
    List for Nagahle Calculation
    0 to 3

    Return:
        list: A list of strings representing the Nagahle
    """
    return [
        "west",
        "north",
        "east",
        "south"
    ]


def set_mahabote():
    """ 
    List for Mahabote Calculation
    0 to 6

    Return:
        list: A list of strings representing the Mahabote
    """
    return [
        "Binga",
        "Atun",
        "Yaza",
        "Adipati",
        "Marana",
        "Thike",
        "Puti"
    ]


def set_nakhat():
    """ 
    List for Nakhat Calculation
    0 to 2

    Return:
        list: A list of strings representing the Nakhat
    """
    return [
        "Ogre",
        "Elf",
        "Human"
    ]


def set_some_astro():
    """ 
    Bool list for cal of some astro

    thamanyo, amyeittasote, warameittugyi
    warameittunge, yatpote,  thamaphyu
    nagapor, yatpote, mahayatkyan, shanyat

    Return:
        list:
    """
    return [
        "true",
        "false"
    ]


def set_moon_phase():
    return [
        "Waxing",
        "Full Moon",
        "Waning",
        "New Moon",
    ]
