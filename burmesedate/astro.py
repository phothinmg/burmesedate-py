# /* cSpell:disable */
"""
Checking Astrological days

More details @ http://cool-emerald.blogspot.sg/2013/12/myanmar-astrological-calendar-days.html

"""

import math
import sys
from .burme import calculate_month_length, julian_to_burmese


def calculate_sabbath(md: int, mm: int, myt: int) -> int:
    """
    Get sabbath day and sabbath eve from day of the month, month, and year type.

    Args:
        md (int) : day in month [1-30]
        mm (int) : month
        myt (int): year type

    Return:
        int : [0 = false, 1 = sabbath, 2 = sabbath_eve]

    """
    mml = calculate_month_length(mm, myt)
    s = 0
    if md in [8, 15, 23, mml]:
        s = 1
    elif md in [7, 14, 22, mml - 1]:
        s = 2
    return s


def calculate_yatyaza(mm: int, wd: int) -> int:  # first waso is considered waso
    """
    Get yatyaza from month, and weekday

    Args:
        mm (int) : month
        wd (int) : weekday [0=sat, 1=sun, ..., 6=fri]

    Return:
        (int): 0 = false , 1 = yatyaza
    """
    m1 = mm % 4
    yatyaza = 0
    wd1 = (m1 // 2) + 4
    wd2 = (1 - (m1 // 2) + (m1 % 2)) * (1 + 2 * (m1 % 2))
    if wd in [wd1, wd2]:
        yatyaza = 1
    return yatyaza


def calculate_pyathada(mm: int, wd: int) -> int:  # first waso is considered waso
    """
    Get pyathada from month, and weekday

    Args:
        mm (int) : month
        wd (int) : weekday [0=sat, 1=sun, ..., 6=fri]

    Return:
        (int): 0 = false , 1=pyathada, 2=afternoon pyathada

    """
    m1 = mm % 4
    pyathada = 0
    wda = [1, 3, 3, 0, 2, 1, 2]
    if m1 == 0 and wd == 4:
        pyathada = 2
    if m1 == wda[wd]:
        pyathada = 1
    return pyathada


def calculate_nagahle(mm: int) -> int:
    """
    Nagahle

    Args:
        mm (int) : month

    Return:
        (int) : 0 = west, 1 = north, 2 = east, 3 = south
    """
    if mm <= 0:
        mm = 4
    return math.floor((mm % 12) / 3)


def calculate_mahabote(my: int, wd: int) -> int:
    """
    Calculate the mahabote value for a given year and weekday.

    Args:
        my (int): The year.
        wd (int): The weekday (0 = Saturday, 1 = Sunday, ..., 6 = Friday).

    Returns:
        (int): The mahabote -> 0 = Binga, 1 = Atun, 2 = Yaza, 
        3 = Adipati, 4 = Marana, 5 = Thike, 6 = Puti.
    """
    return (my - wd) % 7


def calculate_nakhat(my: int) -> int:
    """
    Calculate Nakhat

    Args:
        my (int): The year.

    Return:
        (int) : 0 = Ogre, 1 = Elf, 2 = Human
    """
    return my % 3


# ===========================================================================================


def calculate_thamanyo(mm: int, wd: int) -> int:
    """
    Calculates the value of 'thamanyo' based on the inputs 'mm' and 'wd'.

    Args:
        mm (int): The month.
        wd (int): The weekday.

    Returns:
        int: The calculated value of 'thamanyo'.1 = thamanyo, 0 = false
    """
    mmt = mm // 13
    mm = (mm % 13) + mmt
    if mm <= 0:
        mm = 4
    thamanyo = 0
    m1 = mm - 1 - mm // 9
    wd1 = (m1 * 2 - m1 // 8) % 7
    wd2 = (wd + 7 - wd1) % 7
    if wd2 <= 1:
        thamanyo = 1
    return thamanyo


def calculate_amyeittasote(md: int, wd: int) -> int:
    """
    Calculates the value of amyeittasote based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of amyeittasote.
    """
    mf = md % 16  # Calculate the fortnight day [0-15]
    amyeittasote = 0  # Initialize amyeittasote
    wda = [5, 8, 3, 7, 2, 4, 1]

    if mf == wda[wd]:
        amyeittasote = 1

    return amyeittasote


def calculate_warameittugyi(md: int, wd: int) -> int:
    """
    Calculates the value of warameittugyi based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of warameittugyi
    """
    mf = md % 16  # Calculate the fortnight day [0-15]
    warameittugyi = 0  # Initialize warameittugyi
    wda = [7, 1, 4, 8, 9, 6, 3]

    if mf == wda[wd]:
        warameittugyi = 1

    return warameittugyi


def calculate_warameittunge(md: int, wd: int) -> int:
    """
    Calculates the value of warameittunge based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of warameittunge
    """
    mf = md % 16  # Calculate the fortnight day [0-15]
    warameittunge = 0  # Initialize warameittunge
    wn = (wd + 6) % 7

    if 12 - mf == wn:
        warameittunge = 1

    return warameittunge


def calculate_yatpote(md: int, wd: int) -> int:
    """
    Calculates the value of yatpote based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of yatpote
    """
    mf = md % 16  # Calculate the fortnight day [0-15]
    yatpote = 0  # Initialize yatpote
    wda = [8, 1, 4, 6, 9, 8, 7]

    if mf == wda[wd]:
        yatpote = 1

    return yatpote


def calculate_thamaphyu(md: int, wd: int) -> int:
    """
    Calculates the value of thamaphyu based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of thamaphyu
    """
    mf = md % 16  # Calculate the fortnight day [0-15]
    thamaphyu = 0  # Initialize thamaphyu
    wda = [1, 2, 6, 6, 5, 6, 7]
    if mf == wda[wd]:
        thamaphyu = 1
    wdb = [0, 1, 0, 0, 0, 3, 3]
    if mf == wdb[wd]:
        thamaphyu = 1
    if mf == 4 and wd == 5:
        thamaphyu = 1
    return thamaphyu


def calculate_nagapor(md: int, wd: int) -> int:
    """
    Calculates the value of nagapor based on the inputs md and wd.

    Args:
        md (int): The month day.
        wd (int): The weekday.

    Returns:
        int: The calculated value of nagapor.
    """
    nagapor = 0
    wda = [26, 21, 2, 10, 18, 2, 21]
    wdb = [17, 19, 1, 0, 9, 0, 0]

    if md in [wda[wd], wdb[wd]]:
        nagapor = 1
    elif (md == 2 and wd == 1) or (md in [12, 4, 18] and wd == 2):
        nagapor = 1

    return nagapor


def calculate_yatyotema(mm: int, md: int) -> int:
    """
    Calculates the value of yatyotema based on the inputs mm and md.

    Args:
        mm (int): The month.
        md (int): The month day.

    Returns:
        int: The calculated value of yatyotema.
    """
    mmt = mm // 13
    mm = (mm % 13) + mmt  # to 1-12 with month type
    if mm <= 0:
        mm = 4  # first waso is considered waso
    mf = md - 15 * (md // 16)  # get fortnight day [0-15]
    yatyotema = 0
    m1 = mm if mm % 2 else (mm + 9) % 12
    m1 = ((m1 + 4) % 12) + 1
    if mf == m1:
        yatyotema = 1
    return yatyotema


def calculate_mahayatkyan(mm: int, md: int) -> int:
    """
    Calculates the value of `mahayatkyan` based on the inputs `mm` and `md`.

    Args:
        mm (int): The month.
        md (int): The month day.

    Returns:
        int: The calculated value of `mahayatkyan`.
    """
    if mm <= 0:
        mm = 4  # first waso is considered waso
    mf = md - 15 * math.floor(md / 16)  # get fortnight day [0-15]
    mahayatkyan = 0
    m1 = ((math.floor((mm % 12) / 2) + 4) % 6) + 1
    if mf == m1:
        mahayatkyan = 1
    return mahayatkyan


def calculate_shanyat(mm: int, md: int) -> int:
    """
    Calculates the value of 'shanyat' based on the inputs 'mm' and 'md'.

    Args:
        mm (int): The month.
        md (int): The month day.

    Returns:
        int: The calculated value of 'shanyat'.
    """
    mmt = mm // 13
    mm = (mm % 13) + mmt  # to 1-12 with month type
    if mm <= 0:
        mm = 4  # first waso is considered waso
    mf = md - 15 * (md // 16)  # get fortnight day [0-15]
    shanyat = 0
    sya = [8, 8, 2, 2, 9, 3, 3, 5, 1, 4, 7, 4]
    if mf == sya[mm - 1]:
        shanyat = 1
    return shanyat


def calculate_astro_days(jd: float) -> list:
    """
    Calculates the astrological days based on a given Julian Day Number (jd).

    Args:
        jd (float): The Julian Day Number for which the astrological days are to be calculated.

    Returns:
        list: A list of strings representing the calculated 
        astrological days for the given Julian Day Number.
    """
    jdn = round(jd)
    hs = []
    yo = julian_to_burmese(jdn)
    mm = yo["mm"]
    md = yo["md"]
    wd = (jdn + 2) % 7

    if calculate_thamanyo(mm, wd):
        hs.append("Thamanyo")
    if calculate_amyeittasote(md, wd):
        hs.append("Amyeittasote")
    if calculate_warameittugyi(md, wd):
        hs.append("Warameittugyi")
    if calculate_warameittunge(md, wd):
        hs.append("Warameittunge")
    if calculate_yatpote(md, wd):
        hs.append("Yatpote")
    if calculate_thamaphyu(md, wd):
        hs.append("Thamaphyu")
    if calculate_nagapor(md, wd):
        hs.append("Nagapor")
    if calculate_yatyotema(mm, md):
        hs.append("Yatyotema")
    if calculate_mahayatkyan(mm, md):
        hs.append("Mahayatkyan")
    if calculate_shanyat(mm, md):
        hs.append("Shanyat")

    return hs


# ========================================================


