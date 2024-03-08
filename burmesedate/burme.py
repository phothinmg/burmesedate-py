"""
# Getting Burmese Calendar Data

---

## Burmese Calendar Eras

| Era            	| Description                  	| Definition                            	|
|----------------	|------------------------------	|---------------------------------------	|
| The first era  	| The era of Myanmar kings     	| 1216 ME (1854 CE) and before          	|
| The second era 	| The era under British colony 	| 1217 ME - 1311 ME (1855 CE - 1949 CE) 	|
| The third era  	| The era after Independence   	| 1312 ME (1950 CE) and after           	|

`burmethon.burme.get_my_const`
---

## Month in Burmese Calendar 

- myt = 0 ->  common year

- myt = 1 ->  year with the intercalary month / little watat

- myt = 2 ->  year with both the intercalary month 
              and the intercalary day / big watat


| **Name**    	| **myt=0** 	| **myt=1** 	| **myt=2** 	| **No.** 	|
|-------------	|:---------:	|:---------:	|:---------:	|---------	|
| Tagu        	|     29    	|     29    	|     29    	| 1       	|
| Kason       	|     30    	|     30    	|     30    	| 2       	|
| Nayon       	|     29    	|     29    	|   **30**  	| 3       	|
| 1st Waso    	|           	|   **30**  	|   **30**  	| 0       	|
| Waso        	|     30    	|     30    	|     30    	| 4       	|
| Wagaung     	|     29    	|     29    	|     29    	| 5       	|
| Tawthalin   	|     30    	|     30    	|     30    	| 6       	|
| Thadingyut  	|     29    	|     29    	|     29    	| 7       	|
| Tazaungmon  	|     30    	|     30    	|     30    	| 8       	|
| Nadaw       	|     29    	|     29    	|     29    	| 9       	|
| Pyatho      	|     30    	|     30    	|     30    	| 10      	|
| Tabodwe     	|     29    	|     29    	|     29    	| 11      	|
| Tabaung     	|     30    	|     30    	|     30    	| 12      	|
| ***Total*** 	| ***354*** 	| ***384*** 	| ***385*** 	|         	|

"""

import math
from typing import List, Tuple


def b1_search(k: int, a: List[Tuple[int, str]]) -> int:
    """
    Perform a binary search on a sorted list of tuples.1 D array

    Parameters:
    - k (int): The key to search for.
    - A (List[Tuple[int, str]]): The sorted list of tuples to search in.

    Returns:
    - int: The index of the found key in the list, or -1 if the key is not found.

    Notes:
    - The function assumes that the list of tuples is sorted in ascending
     order based on the first element of each tuple.
    - The function uses a binary search algorithm to find the key in the list.
    - The function returns the index of the found key in the list,
      or -1 if the key is not found.

    Example:
    >>> b1_search(5, [(1, 'a'), (3, 'b'), (5, 'c'), (7, 'd'), (9, 'e')])
    2
    """
    u = len(a) - 1
    l = 0

    while u >= l:
        i = (l + u) // 2
        z = a[i]

        if z > k:
            u = i - 1
        elif z < k:
            l = i + 1
        else:
            return i

    return -1


def b2_search(k: int, a: List[Tuple[int, str]]) -> int:
    """
    Perform a binary search on a list of tuples.2 D array

    Parameters:
    - k (int): The key to search for.
    - a (List[Tuple[int, str]]): The list of tuples to search in.

    Returns:
    - int: The index of the tuple that matches the key, or -1 if no match is found.

    Notes:
    - The function assumes that the list of tuples is sorted in ascending order
      based on the first element of each tuple.
    - The function uses a binary search algorithm to find the key in the list.
    - The function returns the index of the tuple that matches the key, or -1 if no match is found.

    Example:
    >>> b2_search(5, [(1, 'a'), (3, 'b'), (5, 'c'), (7, 'd'), (9, 'e')])
    2
    """
    u = len(a) - 1
    l = 0

    while u >= l:
        i = (l + u) // 2
        z = a[i][0]

        if z > k:
            u = i - 1
        elif z < k:
            l = i + 1
        else:
            return i

    return -1


def get_my_const(my: int) -> dict:
    """
    ## Return a dictionary of constants based on the given Burmese calendar era.

    ### Parameters:
    - my (int): The Burmese year to check.

    ### Returns:
    - dict: A dictionary containing the following constants:
        - ei (float): Burmese calendar era ID [1-3]
          calculations methods/constants depend on era.
        - wo (float): Watat offset to compensate.
        - nm (int): Number of months to find excess days.
        - ew (int): Exception in watat year.

    ### Notes:
    - The function uses binary search algorithms (b1_search and b2_search)
      to find exceptions in the calendar eras.
    - The constants are determined based on the given Burmese calendar era ID (my).
    - The function returns a dictionary with the calculated constants.

    ### Dependencies
        - `burmethon.helper.main.b1_search`
        - `burmethon.helper.main.b2_search`

    ### Example:

    >>> get_my_const(1312)
    {'ei': 3, 'wo': -0.5, 'NM': 8, 'ew': 0}
    """
    ei = 0
    wo = 0
    nm = 0
    ew = 0

    if my >= 1312:  # The third era (the era after Independence 1312 ME and after)
        ei = 3
        wo = -0.5
        nm = 8
        fme = [[1377, 1]]
        wte = [1344, 1345]
    # The second era (the era under British colony: 1217 ME - 1311 ME)
    elif my >= 1217:
        ei = 2
        wo = -1
        nm = 4
        fme = [[1234, 1], [1261, -1]]
        wte = [1344, 1345]
    # The first era (the era of Burmese kings: ME1216 and before)
    elif my >= 1100:
        # Thandeikta (ME 1100 - 1216)
        ei = 1.3
        wo = -0.85
        nm = -1
        fme = [[1120, 1], [1126, -1], [1150, 1], [1172, -1], [1207, 1]]
        wte = [1201, 1202]
    elif my >= 798:  # Makaranta system 2 (ME 798 - 1099)
        ei = 1.2
        wo = -1.1
        nm = -1
        fme = [
            [205, 1],
            [246, 1],
            [471, 1],
            [572, -1],
            [651, 1],
            [653, 2],
            [656, 1],
            [672, 1],
            [729, 1],
            [767, -1],
        ]
        wte = []
    else:  # Makaranta system 1 (ME 0 - 797)
        ei = 1.1
        wo = -1.1
        nm = -1
        fme = [
            [205, 1],
            [246, 1],
            [471, 1],
            [572, -1],
            [651, 1],
            [653, 2],
            [656, 1],
            [672, 1],
            [729, 1],
            [767, -1],
        ]
        wte = []

    # full moon day offset exceptions
    i = b2_search(my, fme)
    if i >= 0:
        wo += fme[i][1]

    # correct watat exceptions
    i = b1_search(my, wte)
    if i >= 0:
        ew = 1

    return {"ei": ei, "wo": wo, "nm": nm, "ew": ew}


def calculate_watat(my):
    """
    Check watat (intercalary month).

    Parameters:
    - my (int): The year to check.

    Returns:
    - dict: A dictionary containing the following information:
        - fm (float): The full moon day of 2nd Waso in jdn_mm
          (jdn+6.5 for MMT) [only valid when watat=1])
        - watat (int): Intercalary month [1=watat, 0=common].

    Example:
    >>> calculate_watat(1312)
    {'fm': 2459372.0, 'watat': 0}
    """
    # get data for respective era
    sy = 1577917828.0 / 4320000.0  # solar year (365.2587565)
    lm = 1577917828.0 / 53433336.0  # lunar month (29.53058795)
    mo = 1954168.050623  # beginning of 0 ME for MMT
    c = get_my_const(my)  # get constants for the corresponding calendar era
    ta = (sy / 12 - lm) * (12 - c["nm"])  # threshold to adjust
    ed = (sy * (my + 3739)) % lm  # excess day
    if ed < ta:
        ed += lm  # adjust excess days
    # full moon day of 2nd Waso
    fm = round(sy * my + mo - ed + 4.5 * lm + c["wo"])
    tw = 0
    watat = 0  # find watat
    if c["ei"] >= 2:
        # if 2nd era or later find watat based on excess days
        tw = lm - (sy / 12 - lm) * c["nm"]
        if ed >= tw:
            watat = 1
    else:
        # if 1st era, find watat by 19 years metonic cycle
        # Myanmar year is divided by 19 and there is intercalary month
        # if the remainder is 2,5,7,10,13,15,18
        # https://github.com/kanasimi/CeJS/blob/master/data/date/calendar.js#L2330
        watat = (my * 7 + 2) % 19
        if watat < 0:
            watat += 19
        watat = watat // 12

    watat ^= c["ew"]  # correct watat exceptions
    return {"fm": fm, "watat": watat}


def check_year(my):
    """
    Calculate the Myanmar calendar information for a given year.

    Parameters:
    - my (int): Burmese  year.

    Returns:
    - dict: A dictionary containing the following information:
        - myt (int): The year type (0=common, 1=little watat, 2=big watat).
        - tg1 (float): The Julian Day Number for the 1st day of Tagu.
        - fm (float): The Julian Day Number for the full moon day of the 2nd Waso.
        - werr (int): Indicator for any watat discrepancy (0=ok, 1=error).

    myt =year type [0=common, 1=little watat, 2=big watat]
    tg1 = the 1st day of Tagu as jdn_mm (Julian Day Number for MMT)
    fm = full moon day of [2nd] Waso as Julian Day Number
    werr= watat discrepancy [0=ok, 1= error] )
    """
    yd = 0
    nd = 0
    werr = 0
    fm = 0
    y2 = calculate_watat(my)
    y1 = None
    myt = y2["watat"]
    while yd < 3:
        yd += 1
        y1 = calculate_watat(my - yd)
        if y1["watat"] == 1:
            break
    if myt:
        nd = (y2["fm"] - y1["fm"]) % 354
        myt = nd // 31 + 1
        fm = y2["fm"]
        if nd not in (30, 31):
            werr = 1
    else:
        fm = y1["fm"] + 354 * yd

    tg1 = y1["fm"] + 354 * yd - 102
    return {"myt": myt, "tg1": tg1, "fm": fm, "werr": werr}


def julian_to_burmese(jdn):
    """
    Converts a Julian Day Number to a Burmese date.

    Parameters:
    - jdn (float): The Julian Day Number to be converted.

    Returns:
    - dict: A dictionary containing the following information:
        - myt (int): The year type (0=common, 1=little watat, 2=big watat).
        - my (int): The Burmese year.
        - mm (int): The Burmese month.
        - md (int): The day in the Burmese month.

    Notes:
    - The function uses the 'cal_my' function to calculate
      the Burmese year and year type.
    - The Burmese year is calculated based on the Julian Day
      Number and the Burmese calendar parameters.
    - The day count is adjusted based on the Burmese year type and the year length.
    - The month and day in the Burmese calendar are calculated based on the adjusted day count.
    - The function returns a dictionary with the calculated Burmese date information.
    """

    jdn = math.ceil(jdn)  # convert jdn to integer + 0.5
    sy = 1577917828.0 / 4320000.0  # solar year (365.2587565)
    mo = 1954168.050623  # beginning of 0 ME
    my = math.floor((jdn - 0.5 - mo) / sy)  # Burmese year
    yo = check_year(my)  # check year
    dd = jdn - yo["tg1"] + 1  # day count
    b = math.floor(yo["myt"] / 2)
    c = math.floor(1 / (yo["myt"] + 1))  # big wa and common yr
    myl = 354 + (1 - c) * 30 + b  # year length
    mmt = math.floor((dd - 1) / myl)  # month type: late = 1 or early = 0
    dd -= mmt * myl
    a = math.floor((dd + 423) / 512)  # adjust day count and threshold
    mm = math.floor((dd - b * a + c * a * 30 + 29.26) / 29.544)  # month
    e = math.floor((mm + 12) / 16)
    f = math.floor((mm + 11) / 16)
    md = dd - math.floor(29.544 * mm - 29.26) - b * e + c * f * 30  # day
    mm += f * 3 - e * 4 + 12 * mmt  # adjust month numbers for late months
    return {
        "myt": yo["myt"],
        "my": my,
        "mm": mm,
        "md": md,
    }  # myt = year type , my = year , mm = month , md = day in month


def calculate_month_length(mm, myt):
    """
    Calculate the length of a month in the Burmese calendar.

    Parameters:
    - mm (int): month [Tagu=1, Kason=2, Nayon=3,
          1st Waso=0, (2nd) Waso=4, Wagaung=5,
          Tawthalin=6, Thadingyut=7, Tazaungmon=8,
          Nadaw=9, Pyatho=10, Tabodwe=11,
          Tabaung=12, Late Tagu=13, Late Kason=14 ],
    - myt (int): year type [0=common, 1=little watat, 2=big watat]

    Returns:
    - mml (int): The length of the month in days (29 or 30).

    The length of a month in the Burmese calendar is determined
    based on the month number and the Burmese year
    type. The month length is calculated as follows:
    - For months 1, 3, 5, 7, 9, and 11, the length is 30 days.
    - For months 2, 4, 6, 8, 10, and 12, the length is 29 days.
    - For the month 3 (Nayon), if the Burmese year type is even,
      the length is increased by 1 day.

    Example usage:
    >>> calculate_month_length(1, 0)
    30
    >>> calculate_month_length(3, 2)
    31
    >>> calculate_month_length(6, 4)
    29
    """
    mml = 30 - (mm % 2)
    if mm == 3:
        mml += math.floor(myt / 2)  # adjust if Nayon in big watat
    # mml = length of the month [29 or 30 days]
    return mml


def calculate_moon_phase(md: int, mm: int, myt: int) -> int:
    """
    Calculates the moon phase based on the given day,
    month, and year type in the Burmese calendar.

    Args:
        md (int): The day of the month.[1-30]
        mm (int): The month [Tagu=1, Kason=2, Nayon=3, 1st Waso=0,
                  (2nd) Waso=4, Wagaung=5, Tawthalin=6, Thadingyut=7,
                  Tazaungmon=8, Nadaw=9, Pyatho=10, Tabodwe=11, Tabaung=12,
                  Late Tagu=13, Late Kason=14].
        myt (int): The year type [0=common, 1=little watat, 2=big watat].

    Returns:
        int: The moon phase value.
             mp =moon phase [0=waxing, 1=full moon, 2=waning, 3=new moon]
    """
    mml = calculate_month_length(mm, myt)
    mp = math.floor((md + 1) // 16) + math.floor(md // 16) + \
        math.floor(md // mml)
    return mp


def calculate_year_length(myt: int) -> int:
    """
    Calculates the length of a year in t
    he Burmese calendar based on a given input.

    Args:
        myt: [0=common, 1=little watat, 2=big watat].

    Returns:
        An integer representing the length of the year in
        the Burmese calendar.
    """
    return 354 + (1 - math.floor(1 / (myt + 1))) * 30 + math.floor(myt / 2)


def calculate_fortnight_day(md: int) -> int:
    """
    Calculates the day of the fortnight based
    on the given day of the month.

    Args:
        md (int): The day of the month for which
                  the fortnight day needs to be calculated.[1-30]

    Returns:
        int: The day of the fortnight corresponding
             to the given day of the month.[1 to 15]
    """
    fortnights = math.floor(md / 16)
    fortnight_day = md - 15 * fortnights
    return fortnight_day


def calculate_day_in_month(mf: int, mp: int, mm: int, myt: int) -> int:
    """
    Calculates the day in a month in the Burmese calendar
    based on the given parameters.

    Args:
        mf (int): [1-15]
        mp (int): [0=waxing, 1=full moon, 2=waning, 3=new moon]
        mm (int): The month [Tagu=1, Kason=2, Nayon=3,
                  1st Waso=0, (2nd) Waso=4, Wagaung=5, Tawthalin=6,
                  Thadingyut=7, Tazaungmon=8, Nadaw=9, Pyatho=10, Tabodwe=11,
                  Tabaung=12, Late Tagu=13, Late Kason=14]
        myt (int): The year type [0=common, 1=little watat, 2=big watat]

    Returns:
        int: The day in the month [1-30]
    """
    mml = calculate_month_length(mm, myt)
    m1 = mp % 2
    m2 = mp // 2
    md = m1 * (15 + m2 * (mml - 15)) + (1 - m1) * (mf + 15 * m2)
    return md


def burmese_to_julian(my: int, mm: int, md: int) -> float:
    """
    Converts a date in the Burmese calendar to the Julian Day Number.

    Args:
        my (int): The Burmese year.
        mm (int): The Burmese month.
        md (int): The Burmese day.

    Returns:
        float: The Julian Day Number corresponding to the given Burmese date.
    """
    b = 0
    c = 0
    dd = 0
    myl = 0
    mmt = 0

    yo = check_year(my)  # check year

    mmt = math.floor(mm // 13)
    mm = (mm % 13) + mmt  # to 1-12 with month type

    b = math.floor(yo["myt"] // 2)
    c = 1 - math.floor((yo["myt"] + 1) // 2)  # if big watat and common year

    mm += 4 - math.floor((mm + 15) // 16) * 4 + \
        ((mm + 12) // 16)  # adjust month

    dd = (
        md
        + math.floor(29.544 * mm - 29.26)
        - c * math.floor((mm + 11) // 16) * 30
        + b * math.floor((mm + 12) // 16)
    )

    myl = 354 + (1 - c) * 30 + b
    dd += mmt * myl  # adjust day count with year length

    return dd + yo["tg1"] - 1
