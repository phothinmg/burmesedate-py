

from burmethon.burmese.genju import julian_to_gregorian, gregorian_to_julian
from burmethon.burmese.burme import julian_to_burmese, calculate_moon_phase, calculate_fortnight_day
from burmethon.burmese.helpers import get_local, jd_now
from burmethon.burmese.translate import translate
from burmethon.burmese.lists import set_weekdays, set_year_types, set_burmese_months, set_moon_phase, set_yatyaza, set_pyathada
import sys
sys.path.append('/home/ptm/Documents/Python-Projects/burmethon')


class burmesedate:

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        self._g2j = gregorian_to_julian(self._year, self._month, self._day)
        self._j2b = julian_to_burmese(self._g2j)
        self._local = get_local()
        self._wekd = self._local["weekday"]
        self._set_wekd = set_weekdays()
        self._moon_phase = set_moon_phase()
        self._set_yrz = set_yatyaza()
        self._set_ptd = set_pyathada()

    @property
    def weekday_eng(self):
        """ 
        Week Day in English

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.weekday_eng)
        """
        return self._set_wekd[self._wekd]

    @property
    def weekday_bur(self):
        """ 
        Week Day in Burmese

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.weekday_bur)
        """
        return translate(self.weekday_eng)

    def _myt(self):
        a = self._j2b['myt']
        return int(a)

    @property
    def year_type_eng(self):
        """ 
        Type of Burmese Year in English

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.year_type_eng)
        """
        a = set_year_types()[self._myt()]
        return a

    @property
    def year_type_bur(self):
        """ 
        Type of Burmese Year in Burmese

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.year_type_bur)
        """
        a = set_year_types()[self._myt()]
        return translate(a)

    def _my(self):
        a = self._j2b['my']
        return int(a)

    @property
    def burmese_year_eng(self):
        """ 
        Burmese Year in English : int

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_year_eng)
        """
        return self._my()

    @property
    def burmese_year_bur(self):
        """ 
        Burmese Year in Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_year_bur)
        """
        a = self._my()
        b = [int(digit) for digit in str(a)]
        f = translate(str(b[0]))
        s = translate(str(b[1]))
        t = translate(str(b[2]))
        fo = translate(str(b[3]))
        fstfo = [f, s, t, fo]
        return ''.join(fstfo)

    def _mm(self):
        a = self._j2b['mm']
        return int(a)

    @property
    def burmese_month_eng(self):
        """ 
        Burmese Month in English : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_month_eng)
        """
        a = self._mm()
        return set_burmese_months()[a]

    @property
    def burmese_month_bur(self):
        """ 
        Burmese Month in Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_month_bur)
        """
        return translate(self.burmese_month_eng)

    def _md(self):
        a = self._j2b['md']
        return int(a)

    @property
    def day_inmonth_eng(self):
        """ 
        Day in month : English : init [1-30]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.day_inmonth_eng)
        """
        return self._md()

    @property
    def day_inmonth_bur(self):
        """ 
        Day in month : Burmese : str [1-30]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.day_inmonth_bur)
        """
        a = self._md()
        b = [int(digit) for digit in str(a)]
        if len(b) == 1:
            return translate(str(b[0]))
        elif len(b) == 2:
            f = translate(str(b[0]))
            s = translate(str(b[1]))
            r = [f, s]
            return ''.join(r)
        else:
            return ''

    def _fortnight_day(self):

        return calculate_fortnight_day(self._md())

    @property
    def fortnight_day_bur(self):
        """ 
        Fortnight Day : Burmese : str [1-15]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.fortnight_day_bur)
        """
        a = self._fortnight_day()
        b = [int(digit) for digit in str(a)]
        if len(b) == 1:
            return translate(str(b[0]))
        elif len(b) == 2:
            f = translate(str(b[0]))
            s = translate(str(b[1]))
            r = [f, s]
            return ''.join(r)
        else:
            return ''

    @property
    def fortnight_day_eng(self):
        """ 
        Fortnight Day : English : int [1-15]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.fortnight_day_eng)
        """
        return self._fortnight_day()

    @property
    def moon_phase_eng(self):
        a = calculate_moon_phase(self._md(), self._mm(), self._myt())
        return self._moon_phase[a]

    @property
    def moon_phase_bur(self):
        return translate(self.moon_phase_eng)


a = burmesedate(2024, 3, 7)
print(a.weekday_bur)
