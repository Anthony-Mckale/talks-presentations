"""import import to_roman_numeral() and to_arabic_number() from roman_numeral_converter.py"""
import pytest

from converter import to_roman_numeral, to_arabic_number


def test_convert_i():
    """simple to_arabic_number (I) == 1"""
    assert to_arabic_number("I") == 1


def test_convert_mmviii():
    """multi to_arabic_number (MMVIII) == 2008"""
    assert to_arabic_number("MMVIII") == 2008


def test_convert_iv():
    """simple subtraction to_arabic_number (IV) == 4"""
    assert to_arabic_number("IV") == 4


def test_convert_xc():
    """subtraction to_arabic_number (XC) == 90"""
    assert to_arabic_number("XC") == 90


def test_convert_mmmcmxcix():
    """big to_arabic_number (MMMCMXCIX) == 3999"""
    assert to_arabic_number("MMMCMXCIX") == 3999


def test_convert_1():
    """simple to_roman_numeral (1) == I"""
    assert to_roman_numeral(1) == "I"


def test_convert_2008():
    """multi to_roman_numeral (2008) == MMVIII"""
    assert to_roman_numeral(2008) == "MMVIII"


def test_convert_4():
    """simple subtraction to_roman_numeral (4) == IV"""
    assert to_roman_numeral(4) == "IV"


def test_convert_90():
    """subtraction to_roman_numeral (90) == XC"""
    assert to_roman_numeral(90) == "XC"


def test_convert_3999():
    """big to_roman_numeral (3999) == MMMCMXCIX"""
    assert to_roman_numeral(3999) == "MMMCMXCIX"


def test_convert_zero():
    """zero fractions to_arabic_number (nulla) == 0"""
    assert to_arabic_number("nulla") == 0

@pytest.mark.skip(reason="not implemented yet")
def test_convert_0():
    """zero fractions to_roman_numeral (0) == nulla"""
    assert to_roman_numeral(0) == "nulla"
