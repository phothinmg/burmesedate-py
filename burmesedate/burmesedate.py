# /* cSpell:disable */

from .genju import *
from .astro import *
from .burme import *
from .helpers import *
from .lists import *
from .translate import *


class burmesedate:

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        self._g2j = gregorian_to_julian(self._year, self._month, self._day)
        self._j2b = julian_to_burmese(self._g2j)
        self._local = get_local()
        self._wekd = self._local["weekday"]
        self._myt = int(self._j2b['myt'])
        self._my = int(self._j2b['my'])
        self._mm =  int(self._j2b['mm'])
        self._md =  int(self._j2b['md'])
        self._fortnight_day = calculate_fortnight_day(self._md)
        self._mp = calculate_moon_phase(self._md, self._mm, self._myt)
        self._yrz = calculate_yatyaza(self._mm, self._wekd)
        self._ptd = calculate_pyathada(self._mm, self._wekd)
        self._sbh = calculate_sabbath(self._md, self._mm, self._myt)
        self._set_wekd = set_weekdays()
        self._moon_phase = set_moon_phase()
        self._set_yrz = set_yatyaza()
        self._set_ptd = set_pyathada()
        self._set_yt = set_year_types()
        self._set_month = set_burmese_months()
        self._set_sbh = set_sabbath()
    
    @property
    def sasana_year_eng(self):
        """ 
        Sasana Year in English : int

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.sasana_year_bur)
        """
        if self._mm == 1 or (self._mm == 2 and self._md < 16):
            buddish_era_offect = 1181
        else: 
            buddish_era_offect = 1182
        return self._my + buddish_era_offect

    @property
    def sasana_year_bur(self):
        """ 
        Sasana Year in Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.sasana_year_bur)
        """
        a = self.sasana_year_eng
        b = [int(digit) for digit in str(a)]
        f = translate(str(b[0]))
        s = translate(str(b[1]))
        t = translate(str(b[2]))
        fo = translate(str(b[3]))
        fstfo = [f, s, t, fo]
        return ''.join(fstfo)


    
    @property
    def year_type_eng(self):
        """ 
        Type of Burmese Year in English

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.year_type_eng)
        """
        a = self._set_yt[self._myt]
        return a

    @property
    def year_type_bur(self):
        """ 
        Type of Burmese Year in Burmese

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.year_type_bur)
        """
        a = self._set_yt[self._myt]
        return translate(a)

    @property
    def burmese_year_eng(self):
        """ 
        Burmese Year in English : int

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_year_eng)
        """
        return self._my

    @property
    def burmese_year_bur(self):
        """ 
        Burmese Year in Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_year_bur)
        """
        a = self._my
        b = [int(digit) for digit in str(a)]
        f = translate(str(b[0]))
        s = translate(str(b[1]))
        t = translate(str(b[2]))
        fo = translate(str(b[3]))
        fstfo = [f, s, t, fo]
        return ''.join(fstfo)

    @property
    def burmese_month_eng(self):
        """ 
        Burmese Month in English : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_month_eng)
        """
        a = self._mm
        return self._set_month[a]

    @property
    def burmese_month_bur(self):
        """ 
        Burmese Month in Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.burmese_month_bur)
        """
        return translate(self.burmese_month_eng)


    @property
    def day_inmonth_eng(self):
        """ 
        Day in month : English : init [1-30]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.day_inmonth_eng)
        """
        return self._md

    @property
    def day_inmonth_bur(self):
        """ 
        Day in month : Burmese : str [1-30]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.day_inmonth_bur)
        """
        a = self._md
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
    def fortnight_day_bur(self):
        """ 
        Fortnight Day : Burmese : str [1-15]

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.fortnight_day_bur)
        """
        a = self._fortnight_day
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
        return self._fortnight_day

    @property
    def moon_phase_eng(self):
        """ 
        Moon Phase : English : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.moon_phase_eng)
        """
        return self._moon_phase[self._mp]

    @property
    def moon_phase_bur(self):
        """ 
        Moon Phase : Burmese : str

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.moon_phase_eng)
        """
        return translate(self.moon_phase_eng)

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

    @property
    def yatyaza_pyathada_eng(self):
        """ 
        Yatyaza - Pyathada : English 

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.yatyaza_pyathada_eng)
        """
        y = self._set_yrz[self._yrz]
        p = self._set_ptd[self._ptd]
        if self._yrz != 0 and self._yrz == 1:
            string = y
        elif self._ptd != 0 and (self._ptd ==1 or self._ptd == 2):
            string = p
        else:
            string = ' '
        return string

    @property
    def yatyaza_pyathada_bur(self):
       """ 
        Yatyaza - Pyathada : English 

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.yatyaza_pyathada_eng)
        """
       return translate(self.yatyaza_pyathada_eng)

    @property
    def sabbath_eng(self):
        """ 
        Sabbath : English

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.sabbath_eng)
        """
        sbh = self._set_sbh[self._sbh]
        if self._sbh != 0 and (self._sbh == 1 and self._sbh == 2):
            string = sbh
        else:
            string = ''
        return string

    @property
    def sabbath_bur(self):
        """ 
        Sabbath : Burmese

        >>> burmesedate = burmesedate(year, month, day)
        >>> print(burmesedate.sabbath_eng)
        """
        return translate(self.sabbath_bur)



