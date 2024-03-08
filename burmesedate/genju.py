import datetime


def gregorian_to_julian(year: int, month: int, day: int) -> float:
    """
    Convert Gregorian date to Julian date.

    Args:
        year (int): The year of the Gregorian date.
        month (int): The month of the Gregorian date.
        day (int): The day of the Gregorian date.

    Returns:
        float: The Julian date corresponding to the input Gregorian date.
    """
    gregorian_date = datetime.date(year, month, day)
    julian_date = gregorian_date.toordinal() + 1721425.5
    return julian_date


def julian_to_gregorian(julian_date: float) -> datetime.date:
    """
    Convert a Julian date to a Gregorian date.

    Args:
        julian_date (float): The Julian date to be converted to a Gregorian date.

    Returns:
        datetime.date: The Gregorian date corresponding to the input Julian date.
    """
    gregorian_date = datetime.date.fromordinal(int(julian_date) - 1721425)
    return gregorian_date
