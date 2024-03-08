"""
Helper Functions
"""

import datetime
from typing import List
from typing import Dict
import pytz
import requests


def unix_to_julian(ut: int) -> float:
    """
    Converts a Unix timestamp to a Julian date.

    Args:
        ut (int): The Unix timestamp to be converted to a Julian date.

    Returns:
        float: The Julian date corresponding to the input Unix timestamp.
    """
    # number of seconds from 1970 Jan 1 00:00:00 (UTC)
    jd = 2440587.5 + ut / 86400.0
    return jd


def julian_to_unix(jdn: float) -> float:
    """
    Converts a Julian date to a Unix timestamp.

    Args:
        jdn (float): The Julian date to be converted to a Unix timestamp.

    Returns:
        float: The Unix timestamp corresponding to the input Julian date.
    """
    unix_timestamp = (jdn - 2440587.5) * 86400.0 + 0.5
    return unix_timestamp


def get_local() -> dict:
    """
    Retrieves the current date, time, and other information in the local timezone.

    Returns:
        dict: A dictionary with the following keys:
            - 'ofs': the offset in seconds between UTC and the local timezone.
            - 'ofm': the offset in minutes between UTC and the local timezone.
            - 'ofh': the offset in hours between UTC and the local timezone.
            - 'ofstr': the string representation of the local timezone.
            - 'weekday': the name of the weekday based on the local date.
            - 'datetime': the formatted date and time in the local timezone.
    """
    # Get the current date and time in UTC
    utc_now = datetime.datetime.now(pytz.utc)
    # Convert UTC time to the local timezone
    local_now = utc_now.astimezone()
    offset = local_now.utcoffset()
    offset_seconds = offset.total_seconds()
    offset_minutes = offset_seconds / 60
    offset_hours = offset_minutes / 60
    offset_str = str(local_now.tzinfo)
    weekday = local_now.weekday()
    date_time = local_now.strftime("%c")
    unix = local_now.timestamp()

    return {
        "ofs": offset_seconds,
        "ofm": offset_minutes,
        "ofh": offset_hours,
        "ofstr": offset_str,
        "weekday": weekday,
        "datetime": date_time,
        "unixtime": unix,
    }


def get_timezones() -> List[str]:
    """
    Retrieves a list of timezones from the World Time API.

    Returns:
        List[str]: A list of timezones in JSON format.
    """
    response = requests.get("http://worldtimeapi.org/api/timezone", timeout=5)
    return response.json()


def get_tz_info(tz: str) -> Dict[str, str]:
    """
    Retrieves information about a timezone using the World Time API.

    Args:
        tz (str): The timezone abbreviation.

    Returns:
        dict: A dictionary containing information about the timezone.
    """
    response = requests.get(f"http://worldtimeapi.org/api/{tz}", timeout=5)
    info = response.json()

    return {
        "abbr": info["abbreviation"],
        "ip": info["client_ip"],
        "datetime": info["datetime"],
        "day_of_week": info["day_of_week"],
        "day_of_year": info["day_of_year"],
        "dst": info["dst"],
        "dst_form": info["dst_from"],
        "dst_util": info["dst_until"],
        "dst_offset": info["dst_offset"],
        "raw_offset": info["raw_offset"],
        "utc_datetime": info["utc_datetime"],
        "unixtime": info["unixtime"],
        "week_number": info["week_number"],
        "utc_offset": info["utc_offset"],
    }


def jd_now() -> float:
    """
    Calculates the Julian date corresponding to the current date and time in the local timezone.

    Returns:
        float: The Julian date corresponding to the current date and time in the local timezone.
    """
    unix = get_local()["unixtime"]
    return unix_to_julian(unix)
